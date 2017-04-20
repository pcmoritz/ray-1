from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import tensorflow.contrib.slim as slim

def vision_net(inputs, num_classes=10):
  conv1 = slim.conv2d(inputs, 64, [4, 4], 2, scope="conv1")
  conv2 = slim.conv2d(conv1, 64, [3, 3], 1, scope="conv2")
  conv3 = slim.conv2d(conv2, 64, [3, 3], 1, scope="conv3")
  conv4 = slim.conv2d(conv3, 64, [3, 3], 1, scope="conv4")
  conv5 = slim.conv2d(conv4, 64, [3, 3], 1, scope="conv5")
  conv6 = slim.conv2d(conv5, 128, [3, 3], 1, scope="conv6")
  conv7 = slim.conv2d(conv6, 128, [3, 3], 1, scope="conv7")
  conv8 = slim.conv2d(conv7, 128, [3, 3], 1, scope="conv8")
  conv9 = slim.conv2d(conv8, 128, [3, 3], 1, scope="conv9")
  flat = tf.reshape(conv9, [-1, 2 * 4 * 4 * 6400])
  fc1 = slim.fully_connected(flat, 512, scope="fc1")
  fc2 = slim.fully_connected(fc1, 512, scope="fc2")
  fc3 = slim.fully_connected(fc2, 512, scope="fc3")
  fc4 = slim.fully_connected(fc3, 512, scope="fc4")
  fc5 = slim.fully_connected(fc4, 512, scope="fc5")
  fc6 = slim.fully_connected(fc5, 512, scope="fc6")
  fc7 = slim.fully_connected(fc6, num_classes, activation_fn=None, normalizer_fn=None, scope="fc7")
  return fc7
