import tensorflow as tf
from game import *
from numpy import array

class Session(object):
    def __init__(self):
        self.game = Game()
        self.initNetwork()

    def initNetwork(self):
        self._input =  tf.placeholder("float", [None, Constants.INPUT_NEURONS_COUNT],  name="input_data")
        self._output = tf.placeholder("float", [None, Constants.OUTPUT_NEURONS_COUNT], name="output_data")

        self._weights = {
            'input_weights':  tf.Variable(tf.random_normal([Constants.INPUT_NEURONS_COUNT,  Constants.INPUT_NEURONS_COUNT]),  name="input_weights"),
            'hidden_weights': tf.Variable(tf.random_normal([Constants.INPUT_NEURONS_COUNT,  Constants.HIDDEN_NEURONS_COUNT]), name="hidden_weights"),
            'output_weights': tf.Variable(tf.random_normal([Constants.HIDDEN_NEURONS_COUNT, Constants.OUTPUT_NEURONS_COUNT]), name="output_weights")
        }

        self._biases = {
            'input_biases':  tf.Variable(tf.random_normal([Constants.INPUT_NEURONS_COUNT]),  name="input_weights"),
            'hidden_biases': tf.Variable(tf.random_normal([Constants.HIDDEN_NEURONS_COUNT]), name="hidden_biases"),
            'output_biases': tf.Variable(tf.random_normal([Constants.OUTPUT_NEURONS_COUNT]), name="output_biases")
        }

        self._inputActivationFunction  = tf.nn.tanh((tf.matmul(self._input,                    self._weights['input_weights'])  + self._biases['input_biases']),  name="input_act_func")
        self._hiddenActivationFunction = tf.nn.tanh((tf.matmul(self._inputActivationFunction,  self._weights['hidden_weights']) + self._biases['hidden_biases']), name="hidden_act_func")
        self._outputActivationFunction = tf.nn.tanh((tf.matmul(self._hiddenActivationFunction, self._weights['output_weights']) + self._biases['output_biases']), name="output_act_func")

        self._tfSession = tf.Session() 
        self._tfSession.run(tf.global_variables_initializer())

    def nextTurn(self):
        self.game.nextTurn(Direction.UP)