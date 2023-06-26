from fitness import fitness
import random
import string
from selection import selection
from crossover import crossover

NUM_OF_WEIGTHS_IN_SET = 84  # 16x4 + 4x4 + 4x1
INIT_NUM_OF_WEIGHTS = 100


def string_to_array(input_string):
    array = []

    for char in input_string:
        array.append(int(char))

    return array


def generate_solution():
    min_val = -1.0
    max_val = 1.0
    random_floats = [random.uniform(min_val, max_val) for _ in range(NUM_OF_WEIGTHS_IN_SET)]
    return random_floats


def encode():
    return generate_solution()


def initialization():
    weights_array = []
    for _ in range(INIT_NUM_OF_WEIGHTS):
        weights_set = encode()
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
        all_weights_updated.append((s, fitness(string_to_array(s), input_data, results)))

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


def ald_main():
    all_dict = []
    best_dict_progress = []
    average_dict_progress = []
    worst_dict_progress = []
    for j in range(1000):
        str = encode()
        all_dict.append(str)
    enc_file_contents, dict_file, dict_file_set, enc_file, freq_dict = generate_dict_from_files()
    for gen in range(350):
        new_generation = []
        temp_worst_sol = []
        temp_top_sol = []
        top_solution, worst_solution = fitness_calculate(all_dict, enc_file_contents, dict_file, dict_file_set,
                                                         enc_file, freq_dict)

        for sol in top_solution:
            temp_top_sol.append(sol[0])

        for sol in worst_solution:  # put all worst sol in one list
            temp_worst_sol.append(sol[0])  # 80

        # STEP 1 - SAVE TOP 20 TO NEXT GENERATION // 20 saved so far
        i = 0
        for sol in top_solution:  # enter only the top to next gen
            i += 1
            new_generation.append(sol[0])  # len is 20
            if i == 50:
                break

        # STEP 2 - SAVE TOP 20 WITH MUTATION  // 25 saved so far
        top_with_mutation = mutation_stage(temp_top_sol, 4)
        new_generation += top_with_mutation  # add top with mutation //25

        # STEP 3 - SAVE TOP 20 WITH CROSSOVER  // 60 saved so far
        new_generation = cross_stage(temp_top_sol, new_generation)  # add top crossover //45

        # STEP 4 -  SAVE NEW 400 // 65 saved so far
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

        all_dict = new_generation

        best_dict_progress.append(top_solution[0][1])
        average_dict_progress.append(worst_solution[40][1])
        worst_dict_progress.append(worst_solution[79][1])

    print("best result: ", all_dict[0])
    # write_results(string_to_dictionary(all_dict[0]))
    return 0

def main():
    w = initialization()  # create 100 weights
    print(w)

if __name__ == "__main__":
    #old_main()
    main()



