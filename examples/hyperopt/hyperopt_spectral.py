from collections import OrderedDict
import itertools
import glmnet
import numpy as np
import random

d = 2

config = OrderedDict([("optimizer", (-1.0, 1.0)), # -1.0 is SGD, 1.0 is ADAM
                      ("learning_rate", (0.01, 0.003, 0.001, 0.0003, 0.0001, 0.00003)),
                      ("dropout_keep_prob", (0.5, 1.0)),
                      ("layer1_filter_size", (4, 5, 6)),
                      ("layer2_filter_size", (4, 5, 6)),
                      ("layer1_num_filters", (16, 32, 64)),
                      ("layer2_num_filters", (16, 32, 64)),
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

def form_matrix(params):
  T = len(params)
  X = np.zeros((T, len(params[0])))
  for i in range(T):
    X[i, :] = np.array(list(params[i].values()))
  return X

# list(zip(np.array(indices)[m.coef_path_[:,-1] != 0.0], m.coef_path_[:,-1][m.coef_path_[:,-1] != 0.0]))

def polynomial_sparse_recovery(X, b, d=1, plot=True):
  T = X.shape[0] # number of random experiments
  n = X.shape[1] # number of hyperparameters
  indices = []
  for k in range(1, d+1):
    indices.extend(itertools.combinations_with_replacement(range(n), k))
  A = np.zeros((T, len(indices)))
  for i in range(T):
    for j in range(len(indices)):
      A[i, j] = np.product(X[i, indices[j]])
  m = glmnet.ElasticNet()
  m.fit(A, b)
  if plot:
    import matplotlib.pyplot as plt
    colors = itertools.cycle(['b', 'r', 'g', 'c', 'k'])
    neg_log_lamda_path = -np.log10(m.lambda_path_)
    for coeff, c in zip(m.coef_path_, colors):
      l1 = plt.plot(neg_log_lamda_path, coeff, c=c)
    plt.xlabel('-Log(alpha)')
    plt.ylabel('coefficients')
    plt.title('Lasso and Elastic-Net Paths')
    plt.axis('tight')
  """
  import IPython
  IPython.embed()
  """
  return m, indices

def execute_rounds(function, args, num_workers):
  arg_iter = iter(args)
  result_dict = dict()
  active_tasks = []
  # Launch set of initial tasks
  for worker_index in range(num_workers):
    arg = next(arg_iter)
    result_id = function.remote(worker_index, *arg)
    active_tasks.append(result_id)
    result_dict[result_id] = arg
  # Wait for tasks being finished and launch new ones
  for arg in arg_iter:
    [finished_id], _ = ray.wait(active_tasks)
    worker_index = active_tasks.index(finished_id)
    result_id = function.remote(worker_index, *arg)
    active_tasks[worker_index] = result_id
    result_dict[result_id] = arg
  return result_dict

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

  params = [sample_params(config) for i in range(128)]
  
  args = [(param, 2000, train_images, train_labels, validation_images, validation_labels) for param in params]
  result_dict = execute_rounds(mnist.train_cnn_and_compute_accuracy, args, 16)
  # accuracy_ids = [mnist.train_cnn_and_compute_accuracy.remote(params[i], 2000, train_images, train_labels, validation_images, validation_labels, str(i % 16)) for i in range(len(params))]

  results = []
  for result_id, args in result_dict.items():
    try:
      results.append((ray.get(result_id)[0], args[0]))
    except:
      results.append(None)

  [accuracy[0] for accuracy in ray.get(accuracy_ids)]
  params
  
  
