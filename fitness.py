# calc fitness by appearances in the dict.txt
def fit_by_dict(word_list, dict, len):
    counter = 0
    for word in word_list:
        if word in dict:
            counter += 1
    return counter

# calc fitness by appearances in the leter2freq
def fit_by_letter_freq(word_list, freq_dict):
    counter = 0
    for word in word_list:
        for i in range(0, len(word)-1):
            counter += freq_dict[word[i:i + 2]]
    return counter

#calculate the fittness of the solution
def fitness(solution, enc_file_contents, dict_file, dict_file_set, enc_file, freq_dict):
    decrypeted_words = []
    for word in enc_file_contents:
        new_word = ""
        for char in word:
            new_word += solution[char] # translate using the dict solution
        decrypeted_words.append(new_word)
    freq_fitness = fit_by_letter_freq(decrypeted_words, freq_dict) # calc fitness by appearances in the dict.txt
    dict_fitness = fit_by_dict(decrypeted_words, dict_file_set, len(decrypeted_words)) # calc fitness by appearances in the leter2freq
    # Close the files
    enc_file.close()
    dict_file.close()
    return dict_fitness + freq_fitness


def generate_dict_from_files():
    # Open the file in read mode
    enc_file_path = 'enc.txt'
    dict_file_path = 'dict.txt'
    letter_freq_file_path = 'Letter2_Freq.txt'
    enc_file = open(enc_file_path, 'r')
    dict_file = open(dict_file_path, 'r')
    letter_freq_file = open(letter_freq_file_path, 'r')
    # Read the entire files contents
    enc_file_contents = enc_file.read().replace(",","").replace(".","").replace(";","").split()
    dict_file_content = dict_file.read().split()
    letter_freq_file_content = letter_freq_file.read().split()
    freq_dict = {}
    # turn th content into a list/dict
    for i in range(0, len(letter_freq_file_content) - 1, 2):
        key = letter_freq_file_content[i + 1].lower()
        value = float(letter_freq_file_content[i])
        freq_dict[key] = value
    dict_file_set = set(dict_file_content)

    return enc_file_contents, dict_file, dict_file_set, enc_file, freq_dict