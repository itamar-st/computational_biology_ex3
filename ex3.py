from fitness import fitness
from createfiles import process_files
import random
import string
from selection import selection
from crossover import crossover

NUM_OF_WEIGTHS_IN_SET = 98  # 16x4 + 4x4 + 4x2 + bias: 4 + 4+ 2
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
        print(len(weights_set))
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
        print(len(s))
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


def main():
    all_solutions = initialization()  # create 100 solutions of 98 cells

    best_sol_progress = []
    average_sol_progress = []
    worst_sol_progress = []

    train_binary_strings, train_labels_encoded, test_binary_strings, test_labels_encoded = \
        process_files('train_set.txt', 'test_set.txt')
    binary_lists = []

    for binary_string in train_binary_strings:
        lst = [int(bit) for bit in binary_string]
        binary_lists.append(lst)

    # Verify the converted numerical representations
    print("Numerical Representations:", binary_lists)

    for gen in range(350):
        new_generation = []
        temp_worst_sol = []
        temp_top_sol = []
        top_solution, worst_solution = fitness_calculate(all_solutions, binary_lists, train_labels_encoded)

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
        top_with_mutation = mutation_stage(temp_top_sol, 4)
        new_generation += top_with_mutation  # add top with mutation //25

        # STEP 3 - SAVE TOP 20 WITH CROSSOVER  // 30 saved so far
        new_generation = cross_stage(temp_top_sol, new_generation)  # add top crossover //45

        # STEP 4 -  SAVE NEW 20 // 65 saved so far
        news = create_x_random_strings(400)
        new_generation += news

        # STEP 5 -  CROSSOVER top with news// 85 saved so far
        top_ten = choose_percentage(25, temp_top_sol)
        news_ten = choose_percentage(12.5, news)
        new_list = top_ten + news_ten

        new_generation = cross_stage(new_list, new_generation)  # 80

        # STEP 6 -  CROSSOVER random tops news// 85 saved so far
        rand_tops = choose_percentage(25, temp_top_sol)
        new_generation = cross_stage(rand_tops, new_generation)

        all_solutions = new_generation

        best_sol_progress.append(top_solution[0][1])
        average_sol_progress.append(worst_solution[40][1])
        worst_sol_progress.append(worst_solution[79][1])

    print("best result: ", all_solutions[0])
    # write_results(string_to_dictionary(all_dict[0]))
    return 0


if __name__ == "__main__":
    main()
