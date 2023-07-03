import json
import numpy as np
import warnings

class NeuralNetwork:
    def __init__(self, weights):  # weights - array[88]
        # Define the number of nodes in each layer

        self.w1 = np.reshape(weights[0:2048], (16, 128))  # 2048 16*128
        self.w2 = np.reshape(weights[2048:10240], (128, 64))  # 8192 128*64
        self.w3 = np.reshape(weights[10240:10368], (64, 2))  # 128 64*2
        # Initialize biases
        self.b1 = np.reshape(weights[10368:10496], (1, 128))  # 128
        self.b2 = np.reshape(weights[10496:10560], (1, 64))  # 64
        self.b3 = np.reshape(weights[10560:10562], (1, 2))  # 2

    def feedforward(self, input_data):
        hidden1 = np.dot(input_data, self.w1) + self.b1
        hidden1 = self.relu(hidden1)

        hidden2 = np.dot(hidden1, self.w2) + self.b2
        hidden2 = self.relu(hidden2)

        output = np.dot(hidden2, self.w3) + self.b3
        output = self.softmax(output)

        return output

    def relu(self, x):
        return np.maximum(0, x)

    def softmax(self, x):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            return np.exp(x) / np.sum(np.exp(x))  # e^x / sumi(e^xi)

    def write_conf_to_file(self, best_result):
        # Create dictionary for network structure
        network_structure = {
            "layers": [
                {"type": "input", "size": 16},
                {"type": "hidden", "size": 128},
                {"type": "hidden", "size": 64},
                {"type": "output", "size": 2}
            ]
        }


        # Create the final data dictionary
        data = {
            "best_result": best_result,
            "network_structure": network_structure
        }

        # Write data to the output file
        with open('wnet0.json', 'w') as output_file:
            json.dump(data, output_file)

