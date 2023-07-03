from fitness import fitness
from createfiles import process_files
import random
from selection import selection
import sys
import NN1

NUM_OF_WEIGTHS_IN_SET = 10562  # 2048 + 8192 + 128 + 128 + 64 + 2
INIT_NUM_OF_WEIGHTS = 100


def string_to_array(input_string):
    array = []

    for char in input_string:
        array.append(int(char))

    return array


def encode():
    min_val = -1.0
    max_val = 1.0
    random_floats = [random.uniform(min_val, max_val) for _ in range(NUM_OF_WEIGTHS_IN_SET)]
    return random_floats


def initialization():
    weights_array = []
    for _ in range(INIT_NUM_OF_WEIGHTS):
        weights_set = encode()
        # print(len(weights_set))
        weights_array.append(weights_set)

    return weights_array


def mutation(s):
    mutated_array = s.copy()
    index = random.randint(0, len(mutated_array) - 1)
    if mutated_array[index] == 0:
        mutated_array[index] = 1
    else:
        mutated_array[index] = 0

    return mutated_array


def choose_percentage(percentage, lst):
    n = int(len(lst) * (percentage / 100))
    selected_items = random.sample(lst, n)
    return selected_items


def fitness_calculate(lst, input_data, results):
    all_weights_updated = []
    for s in lst:
        # print(len(s))
        all_weights_updated.append((s, fitness(s, input_data, results)))

    top_solution, worst_solution = selection(all_weights_updated)

    return top_solution, worst_solution


def cross_stage(lst, new_generation):
    shuffled_list = random.sample(lst, len(lst))
    for i in range(len(shuffled_list) - 1):
        if i == 0:
            new_generation.append(crossover(shuffled_list[i], shuffled_list[-1]))
        x = crossover(shuffled_list[i], shuffled_list[i + 1])
        new_generation.append(x)

    return new_generation


def crossover(solution1, solution2):
    # Generate a random crossover point
    crossover_point = random.randint(1, NUM_OF_WEIGTHS_IN_SET)

    # Perform crossover operation
    new_cross = solution1[:crossover_point] + solution2[crossover_point:]

    return new_cross


def mutation_stage(lst, index):
    for element in lst:
        lst.remove(element)
        for i in range(index):
            temp = element
            n = mutation(temp)
            element = n
        lst.append(element)

    return lst


def create_x_random_strings(x):
    str_lst = []
    for _ in range(x):
        str = encode()
        str_lst.append(str)

    return str_lst


def build_network_structure():
    # Define the network structure
    network_structure = {
        "layers": [
            {"type": "input", "size": 10},
            {"type": "hidden", "size": 20},
            {"type": "output", "size": 5}
        ]
    }
    return network_structure


def build_net(learn_file, testfile):
    all_solutions = initialization()  # create 100 solutions of 98 cells

    best_sol_progress = []
    average_sol_progress = []
    worst_sol_progress = []

    train_binary_strings, train_labels_encoded, test_binary_strings, test_labels_encoded = \
        process_files(learn_file, testfile)

    binary_lists_train = []
    binary_lists_test = []

    for bin_str_train in train_binary_strings:
        lst = [int(bit) for bit in bin_str_train]
        binary_lists_train.append(lst)

    for bin_str_test in test_binary_strings:
        lst = [int(bit) for bit in bin_str_test]
        binary_lists_test.append(lst)

    # Verify the converted numerical representations
    # print("Numerical Representations:", binary_lists_train)
    gen_num = 1
    for gen in range(350):
        print("-------------Generation num: ", gen_num, "----------------------")
        gen_num += 1
        new_generation = []
        temp_worst_sol = []
        temp_top_sol = []
        top_solution, worst_solution = fitness_calculate(all_solutions, binary_lists_train, train_labels_encoded)

        for sol in top_solution:
            temp_top_sol.append(sol[0])

        for sol in worst_solution:  # put all worst sol in one list
            temp_worst_sol.append(sol[0])

        # STEP 1 - SAVE TOP 5 TO NEXT GENERATION // 5 saved so far
        i = 0
        for sol in top_solution:  # enter only the top to next gen
            i += 1
            new_generation.append(sol[0])
            if i == 5:
                break

        # STEP 2 - SAVE TOP 20 WITH MUTATION  // 25 saved so far
        top_with_mutation = mutation_stage(temp_top_sol, 500)
        new_generation += top_with_mutation  # add top with mutation //25

        # STEP 3 - SAVE TOP 20 WITH CROSSOVER  // 30 saved so far
        new_generation = cross_stage(temp_top_sol, new_generation)  # add top crossover //45

        # STEP 4 -  SAVE NEW 20 // 65 saved so far
        # news = create_x_random_strings(20)
        # new_generation += news
        fifteen_worst = choose_percentage(18.75, temp_worst_sol)
        mutation_fifteen_worst = mutation_stage(fifteen_worst, 1000)
        new_generation += mutation_fifteen_worst

        # STEP 5 -  CROSSOVER top with news// 85 saved so far
        fifteen_top_ten = choose_percentage(50, temp_top_sol)
        fifteen_news = create_x_random_strings(10)
        uni_lst = fifteen_top_ten + fifteen_news
        new_generation = cross_stage(uni_lst, new_generation)  # add top crossover //45

        # STEP 6 -  CROSSOVER random worst// 85 saved so far
        news = create_x_random_strings(10)
        top_ten = choose_percentage(50, temp_top_sol)
        u_l = news + top_ten
        new_generation = cross_stage(u_l, new_generation)

        all_solutions = new_generation

        best_sol_progress.append(top_solution[0][1])
        average_sol_progress.append(worst_solution[40][1])
        worst_sol_progress.append(worst_solution[79][1])

    print("best result: ", all_solutions[0])
    # write_results(string_to_dictionary(all_dict[0]))
    print("the test result:")
    fitness(all_solutions[0], binary_lists_test, test_labels_encoded)

    best_result = all_solutions[0]
    network = NN1.NeuralNetwork(best_result)
    network.write_conf_to_file(best_result)

    return 0


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python buildnet.py <learning_file> <test_file>")
        sys.exit(1)

    # Extract the file names from command-line arguments
    learning_file = sys.argv[1]
    test_file = sys.argv[2]

    # Call build_net with the file names
    build_net(learning_file, test_file)
