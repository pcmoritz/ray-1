from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import ray
import tensorflow as tf

class TensorFlowServer(object):

    def __init__(self, model_path, input="inputs", output="classes"):
        self.graph = tf.Graph()
        self.sess = tf.Session(graph=self.graph)
        self.model = tf.saved_model.loader.load(self.sess, ["serve"], model_path)

        serving_default = self.model.signature_def["serving_default"]
        inputs_name = serving_default.inputs[input].name
        outputs_name = serving_default.outputs[output].name

        self.inputs = self.graph.get_tensor_by_name(inputs_name)
        self.outputs = self.graph.get_tensor_by_name(outputs_name)

    def predict(self, inputs, preprocessor=lambda x: x, postprocessor=lambda x: x):
        examples = [preprocessor(input) for input in inputs]
        results = self.sess.run(self.outputs, feed_dict={self.inputs: examples})
        return [postprocessor(result) for result in results]
