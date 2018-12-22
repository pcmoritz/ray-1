# Ray Serving

## Simple Example: Serving MNIST

```python
import tensorflow as tf
import ray.experimental.serving as serving

def _float_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=value.flatten()))

def mnist_to_example(digit):
  return tf.train.Example(
      features=tf.train.Features(
          feature={"x": _float_feature(1.0 * digit)}))

server = serving.TensorFlowServer("/tmp/mnist/1")
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
example = mnist_to_example(x_test[0])
server.predict([example.SerializeToString()])
```
