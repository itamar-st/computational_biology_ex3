import random

from ex2 import string_to_dictionary
from fitness import fitness


def darwinian_or_lamarkian(dict_list, enc_file_contents, dict_file, dict_file_set, enc_file, freq_dict):
    new_dict_list = []
    best_sol =  dict_list[0]
    for d in dict_list:
        after_augmentation_dict = try_augmentations(d[0], best_sol)  # swap N chars
        fitness_of_augmented_dict = fitness(string_to_dictionary(after_augmentation_dict), enc_file_contents, dict_file, dict_file_set, enc_file, freq_dict)
        if fitness_of_augmented_dict > d[1]:  # if the fitness after the augmentation is greater then before
            d = darwinian(d, fitness_of_augmented_dict)
        new_dict_list.append(d)
    return new_dict_list


def darwinian(d, fitness_of_augmented_dict):
    d = (d[0], fitness_of_augmented_dict)
    return d


def lamarkian(after_augmentation_dict, fitness_of_augmented_dict):
    d = (after_augmentation_dict, fitness_of_augmented_dict)
    return d


def try_augmentations(s, best_sol):
    # Generate eight random numbers between 0 and 25
    random_nums = [random.randint(0, 25) for _ in range(4)]

    s = list(s)
    # Perform the swaps using a for loop
    for i in range(0, 4, 2):
        s[random_nums[i]], s[random_nums[i+1]] = s[random_nums[i+1]], s[random_nums[i]]
    # Convert the list back to a string
    return ''.join(s)

