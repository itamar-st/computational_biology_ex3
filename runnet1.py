import numpy as np


class NeuralNetwork:
    def __init__(self, weights):  # weights - array[88]
        # Define the number of nodes in each layer

        # weight = [16*8, 8*8, 8*2]
        # print(weights[0:63])
        self.weights1 = np.reshape(weights[0:128], (16, 8))  # 128 16*8
        self.weights2 = np.reshape(weights[128:192], (8, 8))  # 64 8*8
        self.weights3 = np.reshape(weights[192:208], (8, 2))  # 16 8*2
        # Initialize biases
        self.bias1 = np.reshape(weights[208:216], (1, 8))
        self.bias2 = np.reshape(weights[216:224], (1, 8))
        self.bias3 = np.reshape(weights[224:226], (1, 2))

        # ---------------- new option -------------------
        self.w1 = np.reshape(weights[0:2048], (16, 128))  # 2048 16*128
        self.w2 = np.reshape(weights[2048:10240], (128, 64))  # 8192 128*64
        self.w3 = np.reshape(weights[10240:10368], (64, 2))  # 128 64*2
        # Initialize biases
        self.b1 = np.reshape(weights[10368:10496], (1, 128)) # 128
        self.b2 = np.reshape(weights[10496:10560], (1, 64)) # 64
        self.b3 = np.reshape(weights[10560:10562], (1, 2)) # 2

    def feedforward(self, input_data):
        # Perform the feedforward operation
        hidden1 = np.dot(input_data, self.weights1) + self.bias1
        hidden1 = self.relu(hidden1)

        hidden2 = np.dot(hidden1, self.weights2) + self.bias2
        hidden2 = self.relu(hidden2)

        output = np.dot(hidden2, self.weights3) + self.bias3
        output = self.softmax(output)

        return output

    def ff(self, input_data):
        hidden1 = np.dot(input_data, self.w1) + self.b1
        hidden1 = self.relu(hidden1)

        hidden2 = np.dot(hidden1, self.w2) + self.b2
        hidden2 = self.relu(hidden2)

        output = np.dot(hidden2, self.w3) + self.b3
        output = self.softmax(output)

        return output

    def sigmoid(self, x):
        # Sigmoid activation function
        return 1 / (1 + np.exp(-x))

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x))  # e^x / sumi(e^xi)
