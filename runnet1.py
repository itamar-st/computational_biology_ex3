import numpy as np
class NeuralNetwork:
    def __init__(self, weights): #weights - array[88]
        # Define the number of nodes in each layer
        self.input_size = 16
        self.hidden_size = 4
        self.output_size = 2

        # wheight = [16*4, 4*4, 4*2]
        # self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        # self.weights2 = np.random.randn(self.hidden_size, self.hidden_size)
        # self.weights3 = np.random.randn(self.hidden_size, self.output_size)
        print(weights[0:63])
        self.weights1 = np.reshape(weights[0:64], (16, 4)) #64 16*4
        self.weights2 = np.reshape(weights[64:80], (4, 4)) #16 4*4
        self.weights3 = np.reshape(weights[80:88], (4, 2)) #8 4*2
        # Initialize biases randomly
        self.bias1 = np.reshape(weights[88:92], (1, 4))
        self.bias2 = np.reshape(weights[92:96], (1, 4))
        self.bias3 = np.reshape(weights[96:98], (1, 2))

    def feedforward(self, input_data):
        # Perform the feedforward operation
        hidden1 = np.dot(input_data, self.weights1) + self.bias1
        hidden1 = self.sigmoid(hidden1)

        hidden2 = np.dot(hidden1, self.weights2) + self.bias2
        hidden2 = self.sigmoid(hidden2)

        output = np.dot(hidden2, self.weights3) + self.bias3
        output = self.softmax(output)

        return output

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))  # e^x / sumi(e^xi)

