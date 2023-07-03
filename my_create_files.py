def split_file(file_path, file1_path, file2_path, count1, count2):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    file1_lines = lines[:count1]
    file2_lines = lines[count1:count1 + count2]

    with open(file1_path, 'w') as file1:
        file1.writelines(file1_lines)

    with open(file2_path, 'w') as file2:
        file2.writelines(file2_lines)


file_path = 'nn1.txt'  # Path to the original file
file1_path = 'train_set1.txt'     # Path to the first output file
file2_path = 'test_set1.txt'     # Path to the second output file
count1 = 15000               # Number of lines to be written in the first file
count2 = 5000                # Number of lines to be written in the second file

split_file(file_path, file1_path, file2_path, count1, count2)