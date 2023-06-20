import random
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
INIT_DICTIONARIES_NUM = 5
def crossover_repair(s):
    # Find the letters that are missing from the cross string
    missing_letters = [letter for letter in ALPHABET if letter not in s]

    # Create a mapping of repeated letters to missing letters
    replace_map = {}
    repeated_letters = set()
    for letter in s:
        if letter in repeated_letters:
            if letter not in replace_map:
                replace_map[letter] = missing_letters.pop(0)
            s = s.replace(letter, replace_map[letter], 1)
        else:
            repeated_letters.add(letter)

    return s


def crossover(s1, s2):
    # Generate a random crossover point
    crossover_point = random.randint(1, 25)

    # Perform crossover operation
    new_cross = s1[:crossover_point] + s2[crossover_point:]

    repair_new_cross = crossover_repair(new_cross)

    return repair_new_cross


def order_crossover(parent1, parent2):
    length = len(parent1)
    segment_start = random.randint(0, length - 2)
    segment_end = random.randint(segment_start + 1, length - 1)
    # Copy the segment from string1 to the child
    child = ['' for i in parent1]
    child[segment_start:segment_end + 1] = parent1[segment_start:segment_end + 1]
    # Copy remaining characters from string2 to the child, preserving order of appearance
    index = 0
    for char in parent2:
        if char not in child:
            while child[index] != '':
                index += 1
            child[index] = char

    return ''.join(child)