import NN0


# calculate the fittness of the solution
def fitness(weights, input_data, results):
    correct_result = 0
    # Create an instance of the neural network
    network = NN0.NeuralNetwork(weights)
    for i in range(len(input_data)):
        # Test the network with some input data
        output = network.feedforward(input_data[i])
        if output[0][0] > output[0][1]:
            output = 0
        else:
            output = 1
        if results[i][0] == 1.0:
            res = 0
        else:
            res = 1
        if output == res:
            correct_result += 1
    # how much of the patternes we got correct in precentage
    print(correct_result / len(results))
    return correct_result / len(results)
