import random
from ex3 import NUM_OF_WEIGTHS_IN_SET

def crossover(solution1, solution2):
    # Generate a random crossover point
    crossover_point = random.randint(1, NUM_OF_WEIGTHS_IN_SET)

    # Perform crossover operation
    new_cross = solution1[:crossover_point] + solution2[crossover_point:]

    return new_cross
