from collections import OrderedDict
import itertools
from sklearn.linear_model import lasso_path
import numpy as np
import random

d = 2

config = OrderedDict([("optimizer", ("SGD", "Adam")),
                      ("learning_rate", (0.01, 0.003, 0.001, 0.0003, 0.0001, 0.00003)),
                      ("layer1_num_filters", (16, 32, 64)),
                      ("layer1_num_filters", (16, 32, 64)),
                      ("layer3_num_filters", (512, 1024, 2048)),
                      ("layer1_stddev", (0.001, 0.003, 0.01, 0.03)),
                      ("layer2_stddev", (0.001, 0.003, 0.01, 0.03)),
                      ("layer3_stddev", (0.001, 0.003, 0.01, 0.03)),
                      ("layer4_stddev", (0.001, 0.003, 0.01, 0.03))])

def sample_params(config):
  return OrderedDict([(key, random.choice(val)) for key, val in config.items()])

hyperparameters = {"optimizer": "Adam",
                   "learning_rate": 1e-3,
                   "layer1_num_filters": 32,
                   "layer2_num_filters": 64,
                   "layer3_num_filters": 1024,
                   "layer1_stddev": 0.01,
                   "layer2_stddev": 0.01,
                   "layer3_stddev": 0.01,
                   "layer4_stddev": 0.01}


def polynomial_sparse_recovery(X, b, d=2, plot=False):
  T = X.shape[0] # number of random experiments
  n = X.shape[1] # number of hyperparameters
  indices = []
  for k in range(1, d+1):
    indices.extend(itertools.combinations_with_replacement(range(n), k))
  A = np.zeros((T, len(indices)))
  for i in range(T):
    for j in range(len(indices)):
      A[i, j] = np.product(X[i, indices[j]])
  alphas_lasso, coeffs_lasso, _ = lasso_path(A, b, eps=1e-3)
  if plot:
    import matplotlib.pyplot as plt
    colors = itertools.cycle(['b', 'r', 'g', 'c', 'k'])
    neg_log_alphas_lasso = -np.log10(alphas_lasso)
    for coeff, c in zip(coeffs_lasso, colors):
      l1 = plt.plot(neg_log_alphas_lasso, coeff, c=c)
    plt.xlabel('-Log(alpha)')
    plt.ylabel('coefficients')
    plt.title('Lasso and Elastic-Net Paths')
    plt.axis('tight')
  import IPython
  IPython.embed()

from tensorflow.examples.tutorials.mnist import input_data
import mnist

if __name__ == "__main__":
  # Load the mnist data and turn the data into remote objects.
  print("Downloading the MNIST dataset. This may take a minute.")
  dataset = input_data.read_data_sets("MNIST_data", one_hot=True)
  train_images = ray.put(dataset.train.images.reshape(-1, 28, 28, 1))
  train_labels = ray.put(dataset.train.labels)
  validation_images = ray.put(dataset.validation.images.reshape(-1, 28, 28, 1))
  validation_labels = ray.put(dataset.validation.labels)

  accuracy_id = mnist.train_cnn_and_compute_accuracy.remote(
        hyperparameters, 2000, train_images, train_labels, validation_images,
        validation_labels, "/gpu:0")
