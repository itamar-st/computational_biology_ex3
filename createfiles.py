import random
from sklearn.preprocessing import OneHotEncoder


def process_files(train_file, test_file):
    # Read the lines from the train and test files
    with open(train_file, 'r') as file:
        train_lines = file.readlines()
    with open(test_file, 'r') as file:
        test_lines = file.readlines()

    # Initialize lists to store the binary strings and labels
    train_binary_strings = []
    train_labels = []
    test_binary_strings = []
    test_labels = []

    # Extract binary strings and labels from train lines
    for line in train_lines:
        binary_string, label = line.strip().split()
        train_binary_strings.append(binary_string)
        train_labels.append(int(label))

    # Extract binary strings and labels from test lines
    for line in test_lines:
        binary_string, label = line.strip().split()
        test_binary_strings.append(binary_string)
        test_labels.append(int(label))

    # Perform one-hot encoding on the labels
    encoder = OneHotEncoder(sparse_output=False, categories='auto')
    train_labels_encoded = encoder.fit_transform([[label] for label in train_labels])
    test_labels_encoded = encoder.transform([[label] for label in test_labels])

    return train_binary_strings, train_labels_encoded, test_binary_strings, test_labels_encoded


def create_files(strings_file):
    train_file = 'train_set.txt'
    test_file = 'test_set.txt'

    with open(strings_file, 'r') as file:
        lines = file.readlines()

    random.shuffle(lines)
    split_index = int(0.75 * len(lines))
    train_lines = lines[:split_index]
    test_lines = lines[split_index:]

    with open(train_file, 'w') as file:
        file.writelines(train_lines)

    # Write the test set to the test_file
    with open(test_file, 'w') as file:
        file.writelines(test_lines)


if __name__ == '__main__':
    # create_files('nn0.txt') # create new files

    train_binary_strings, train_labels_encoded, test_binary_strings, test_labels_encoded = \
        process_files('train_set.txt', 'test_set.txt')
    numerical_representations = []
    for binary_string in train_binary_strings:
        numerical_representation = int(binary_string, 2)  # Convert binary string to decimal
        numerical_representations.append(numerical_representation)

    # Verify the converted numerical representations
    print("Numerical Representations:", numerical_representations)
