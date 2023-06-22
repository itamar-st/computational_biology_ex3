import numpy as np
class NeuralNetwork:
    def __init__(self, wheights):
        # Define the number of nodes in each layer
        self.input_size = 16
        self.hidden_size = 4
        self.output_size = 1

        # wheight = [16*4, 4*4, 4*1]
        # self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        # self.weights2 = np.random.randn(self.hidden_size, self.hidden_size)
        # self.weights3 = np.random.randn(self.hidden_size, self.output_size)
        self.weights1 = wheights[0]
        self.weights2 = wheights[1]
        self.weights3 = wheights[2]
        # Initialize biases randomly
        self.bias1 = np.random.randn(self.hidden_size)
        self.bias2 = np.random.randn(self.hidden_size)
        self.bias3 = np.random.randn(self.output_size)

    def feedforward(self, input_data):
        # Perform the feedforward operation
        hidden1 = np.dot(input_data, self.weights1) + self.bias1
        hidden1 = self.sigmoid(hidden1)

        hidden2 = np.dot(hidden1, self.weights2) + self.bias2
        hidden2 = self.sigmoid(hidden2)

        output = np.dot(hidden2, self.weights3) + self.bias3
        output = self.sigmoid(output)

        return output

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))



