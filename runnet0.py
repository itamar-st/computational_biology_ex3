import json
import sys
import numpy as np
import NN0

def parse_json_data(json_data):
    num_layer_types = len(json_data['layers'])
    layer_sizes = [layer['size'] for layer in json_data['layers']]
    return num_layer_types, layer_sizes

def init_network(weights, num_layers_types, layer_sizes):

    bias_num = num_layers_types - 1
    w_num = num_layers_types - 1

    curr_base = 0
    w = []
    b = []

    for i in range(w_num):
        x = layer_sizes[i]
        y = layer_sizes[i+1]
        mat_taple = (x, y)
        curr_top = curr_base + x*y
        wi = np.reshape(weights[curr_base:curr_top], mat_taple)
        w.append(wi)
        curr_base = curr_top

    for j in range(bias_num):
        x = 1
        y = layer_sizes[j+1]
        vec_taple = x*y
        curr_top = curr_base + x*y
        bi = np.reshape(weights[curr_base:curr_top], vec_taple)
        b.append(bi)
        curr_base = curr_top

    return w, b


def feedforward(array_data, w, b):
    hidden1 = np.dot(array_data, w[0]) + b[0]
    hidden1 = relu(hidden1)

    hidden2 = np.dot(hidden1, w[1]) + b[1]
    hidden2 = relu(hidden2)

    output = np.dot(hidden2, w[2]) + b[2]
    output = softmax(output)

    return output


def relu(x):
    return np.maximum(0, x)


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))  # e^x / sumi(e^xi)


def load_weights(file_path, part):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        weights = data[part]
    return weights


# Calculate the fitness of the solution
def fitness(weights, input_data):
    # Create an instance of the neural network
    network = NN0.NeuralNetwork(weights)
    print("fcdfd")
    print(type(weights))
    for i in range(len(input_data)):
        # Test the network with some input data
        output = network.feedforward(input_data[i])
        if output[0][0] > output[0][1]:
            output = 0
        else:
            output = 1

        with open('output0.txt', 'a') as f:
            s = ''.join(str(num) for num in input_data[i])
            f.write(f'{s} {output}\n')


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python buildnet.py <learning_file> <test_file>")
        sys.exit(1)

    # Extract the file names from command-line arguments
    wnet0_file = sys.argv[1]  # json file
    data_file = sys.argv[2]  # text file

    best_res = load_weights(wnet0_file, 'best_result')
    network_structure = load_weights(wnet0_file, 'network_structure')

    # print("best: ")
    print(len(best_res))
    print(best_res)
    print("network_structure: ")
    print(network_structure)

    num_layers_types, layer_sizes = parse_json_data(network_structure)
    print("Number of layer types:", num_layers_types)
    print("Layer sizes:", layer_sizes)
    best_res_len = len(best_res)

    test_data = []

    with open(data_file, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace or newline characters
            test_data.append(line)

    binary_lists = []

    for bin_str in test_data:
        lst = [int(bit) for bit in bin_str]
        binary_lists.append(lst)

    print("fgdg")
    print(binary_lists)

    # w, b = init_network(best_res, num_layers_types, layer_sizes)
    fitness(best_res, binary_lists)

