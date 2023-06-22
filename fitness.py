import runnet1
import numpy as np
#calculate the fittness of the solution
def fitness(wheights,input_data, results):
    correct_result = 0
    # Create an instance of the neural network
    network = runnet1.NeuralNetwork(wheights)
    for i in range(len(input_data)):
        # Test the network with some input data
        output = network.feedforward(input_data[i])
        if output == results[i]:
            correct_result += 1
        print(f"Output: {output}, real value: {results[i]}")
    #how much of the patternes we got correct in precentage
    return correct_result/len(results)
