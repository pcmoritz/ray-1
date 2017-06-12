# Most of the tensorflow code is adapted from Tensorflow's tutorial on using
# CNNs to train MNIST
# https://www.tensorflow.org/versions/r0.9/tutorials/mnist/pros/index.html#build-a-multilayer-convolutional-network.  # noqa: E501

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import ray
import tensorflow as tf

slim = tf.contrib.slim

def get_batch(data, batch_index, batch_size):
  # This method currently drops data when num_data is not divisible by
  # batch_size.
  num_data = data.shape[0]
  num_batches = num_data // batch_size
  batch_index %= num_batches
  return data[(batch_index * batch_size):((batch_index + 1) * batch_size)]


def cnn_setup(params, images, labels, num_classes, is_training=True, scope='LeNet'):
  with tf.variable_scope(scope, 'LeNet', [images, num_classes]):
    net = slim.conv2d(images, params["layer1_num_filters"], [params["layer1_filter_size"], params["layer1_filter_size"]],
                      weights_initializer=tf.truncated_normal_initializer(stddev=params["layer1_stddev"]),
                      scope='conv1')
    net = slim.max_pool2d(net, [2, 2], 2, scope='pool1')
    net = slim.conv2d(net, params["layer2_num_filters"], [params["layer2_filter_size"], params["layer2_filter_size"]],
                      weights_initializer=tf.truncated_normal_initializer(stddev=params["layer2_stddev"]),
                      scope='conv2')
    net = slim.max_pool2d(net, [2, 2], 2, scope='pool2')
    net = slim.flatten(net)

    net = slim.fully_connected(net, params["layer3_num_filters"],
                               weights_initializer=tf.truncated_normal_initializer(stddev=params["layer3_stddev"]),
                               scope='fc3')
    net = slim.dropout(net, params["dropout_keep_prob"], is_training=True, scope='dropout3')
    logits = slim.fully_connected(net, num_classes, activation_fn=None,
                                  weights_initializer=tf.truncated_normal_initializer(stddev=params["layer4_stddev"]),
                                  scope='fc4')
  output = tf.nn.softmax(logits)
  cross_entropy = tf.reduce_mean(-tf.reduce_sum(labels * tf.log(output),
                                 reduction_indices=[1]))
  correct_pred = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
  if params["optimizer"] > 0.0:
    optimizer = tf.train.AdamOptimizer(params["learning_rate"])
  elif params["optimizer"] < 0.0:
    optimizer = tf.train.GradientDescentOptimizer(params["learning_rate"])
  else:
    assert False, "Unknown optimizer {}".format(params["optimizer"])
  return (optimizer.minimize(cross_entropy),
          tf.reduce_mean(tf.cast(correct_pred, tf.float32)), cross_entropy)


# Define a remote function that takes a set of hyperparameters as well as the
# data, consructs and trains a network, and returns the validation accuracy.
@ray.remote(max_num_tasks=1)
def train_cnn_and_compute_accuracy(device, params, steps, train_images, train_labels,
                                   validation_images, validation_labels,
                                   weights=None):
  os.environ["CUDA_VISIBLE_DEVICES"] = str(device)
  # Extract the hyperparameters from the params dictionary.
  batch_size = 128
  # Create the network and related variables.
  tf.reset_default_graph()
  import gc
  gc.collect()
  with tf.Graph().as_default():
    with tf.Session() as sess:
      # Create the input placeholders for the network.
      images = tf.placeholder(tf.float32, shape=[None, 28, 28, 1])
      labels = tf.placeholder(tf.float32, shape=[None, 10])
      # Create the network.
      train_step, accuracy, loss = cnn_setup(params, images, labels, 10)
      # Do the training and evaluation.

      # Use the TensorFlowVariables utility. This is only necessary if we want
      # to set and get the weights.
      variables = ray.experimental.TensorFlowVariables(loss, sess)
      # Initialize the network weights.
      sess.run(tf.global_variables_initializer())
      # If some network weights were passed in, set those.
      if weights is not None:
        variables.set_weights(weights)
      # Do some steps of training.
      for i in range(1, steps + 1):
        # Fetch the next batch of data.
        image_batch = get_batch(train_images, i, batch_size)
        label_batch = get_batch(train_labels, i, batch_size)
        # Do one step of training.
        sess.run(train_step, feed_dict={images: image_batch, labels: label_batch})
      # Training is done, so compute the validation accuracy and the current
      # weights and return.
      totalacc = accuracy.eval(feed_dict={images: validation_images,
                                          labels: validation_labels})
      new_weights = variables.get_weights()
      sess.close()
  return float(totalacc), new_weights
