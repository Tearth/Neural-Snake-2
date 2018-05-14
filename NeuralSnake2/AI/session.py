import tensorflow as tf
import numpy as np
from game import *
from numpy import array

class Session(object):
    def __init__(self, genotype = None):
        self._game = Game()
        self.initNetwork(genotype)

    def initNetwork(self, genotype = None):
        self._input =  tf.placeholder("float", [None, Constants.INPUT_NEURONS_COUNT],  name="input_data")
        self._output = tf.placeholder("float", [None, Constants.OUTPUT_NEURONS_COUNT], name="output_data")
        
        self._lastInput = [0] * Constants.INPUT_NEURONS_COUNT
        self._lastOutput = [0] * Constants.OUTPUT_NEURONS_COUNT
        
        if genotype == None:
            self._initWeightAndBiases()
        else:
            self._initWeightAndBiasesWithGenotype(genotype)

        self._inputActivationFunction  = tf.nn.tanh((tf.matmul(self._input,                    self._weights['input_weights'])  + self._biases['input_biases']),  name="input_act_func")
        self._hiddenActivationFunction = tf.nn.tanh((tf.matmul(self._inputActivationFunction,  self._weights['hidden_weights']) + self._biases['hidden_biases']), name="hidden_act_func")
        self._outputActivationFunction = tf.nn.tanh((tf.matmul(self._hiddenActivationFunction, self._weights['output_weights']) + self._biases['output_biases']), name="output_act_func")

        self._tfSession = tf.Session()

    def nextTurn(self):
        input_values = []
        eyes = self._game.getSnakeEyes()
        nearestFood = self._game.getNearestFoodDirection()

        for eye in eyes:
            input_values.append(eye * 2 - 1)

        for foodDirection in nearestFood:
            input_values.append(foodDirection * 2 - 1)

        input_array = array(input_values).reshape(1, Constants.INPUT_NEURONS_COUNT)
        output_values = self._tfSession.run(self._outputActivationFunction, feed_dict={self._input: input_array})[0]

        direction = output_values.argmax()
        self._game.nextTurn(Direction(direction))

        self._lastInput = input_values
        self._lastOutput = output_values

    def getBoardState(self):
        return self._game.boardfields

    def getSessionInfo(self):
        return {
            'input': self._lastInput,
            'output': self._lastOutput
        }

    def isRunning(self):
        return self._game.running

    def getScore(self):
        return (50 * self._game.getSnakeLength()) + self._game.age

    def _initWeightAndBiases(self):
        self.genotype = [0] * self._getGenotypeLength()
        for i in range(len(self.genotype)):
            self.genotype[i] = uniform(-1, 1)

        self._initWeightAndBiasesWithGenotype(self.genotype)

    def _initWeightAndBiasesWithGenotype(self, genotype):
        self._weights = {
            'input_weights':  tf.Variable(tf.zeros([Constants.INPUT_NEURONS_COUNT,  Constants.INPUT_NEURONS_COUNT]),  name="input_weights"),
            'hidden_weights': tf.Variable(tf.zeros([Constants.INPUT_NEURONS_COUNT,  Constants.HIDDEN_NEURONS_COUNT]), name="hidden_weights"),
            'output_weights': tf.Variable(tf.zeros([Constants.HIDDEN_NEURONS_COUNT, Constants.OUTPUT_NEURONS_COUNT]), name="output_weights")
        }

        self._biases = {
            'input_biases':  tf.Variable(tf.zeros([Constants.INPUT_NEURONS_COUNT]),  name="input_weights"),
            'hidden_biases': tf.Variable(tf.zeros([Constants.HIDDEN_NEURONS_COUNT]), name="hidden_biases"),
            'output_biases': tf.Variable(tf.zeros([Constants.OUTPUT_NEURONS_COUNT]), name="output_biases")
        }

        input_weights = genotype[0:Constants.INPUT_NEURONS_COUNT * Constants.INPUT_NEURONS_COUNT]
        length = len(input_weights)

        hidden_weights = genotype[length:length + Constants.INPUT_NEURONS_COUNT * Constants.HIDDEN_NEURONS_COUNT]
        length += len(hidden_weights)

        output_weights = genotype[length:length + Constants.HIDDEN_NEURONS_COUNT * Constants.OUTPUT_NEURONS_COUNT]
        length += len(output_weights)

        input_biases = genotype[length:length + Constants.INPUT_NEURONS_COUNT]
        length += len(input_biases)

        hidden_biases = genotype[length:length + Constants.HIDDEN_NEURONS_COUNT]
        length += len(hidden_biases)

        output_biases = genotype[length:length + Constants.OUTPUT_NEURONS_COUNT]
        length += len(output_biases)

        self._weights['input_weights'] = tf.assign(self._weights['input_weights'], array(input_weights).reshape(Constants.INPUT_NEURONS_COUNT, Constants.INPUT_NEURONS_COUNT))
        self._weights['hidden_weights'] = tf.assign(self._weights['hidden_weights'], array(hidden_weights).reshape(Constants.INPUT_NEURONS_COUNT, Constants.HIDDEN_NEURONS_COUNT))
        self._weights['output_weights'] = tf.assign(self._weights['output_weights'], array(output_weights).reshape(Constants.HIDDEN_NEURONS_COUNT, Constants.OUTPUT_NEURONS_COUNT))

        self._biases['input_biases'] = tf.assign(self._biases['input_biases'], input_biases)
        self._biases['hidden_biases'] = tf.assign(self._biases['hidden_biases'], hidden_biases)
        self._biases['output_biases'] = tf.assign(self._biases['output_biases'], output_biases)

        self.genotype = genotype

    def _getGenotypeLength(self):
        return (Constants.INPUT_NEURONS_COUNT * Constants.INPUT_NEURONS_COUNT) + \
               (Constants.INPUT_NEURONS_COUNT * Constants.HIDDEN_NEURONS_COUNT) + \
               (Constants.HIDDEN_NEURONS_COUNT * Constants.OUTPUT_NEURONS_COUNT) + \
               (Constants.INPUT_NEURONS_COUNT + Constants.HIDDEN_NEURONS_COUNT + Constants.OUTPUT_NEURONS_COUNT)