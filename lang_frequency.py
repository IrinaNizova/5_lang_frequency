from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, "r") as file_object:
        lines = file_object.readlines()
    return lines

def count_words(lines):
    words_dict = Counter()
    for line in lines:
        match_patterns = re.findall(r'\b\w{2,25}\b', line)
        for word in match_patterns:
            words_dict[word] += 1
    return words_dict


def get_most_frequent_words(words_dict):
    frequent_words_number = 10
    return words_dict.most_common(frequent_words_number)


if __name__ == '__main__':
    lines = load_data(sys.argv[1])
    words_dict = count_words(lines)
    for word in get_most_frequent_words(words_dict):
        print('{} found {} times'.format(word[0], word[1]))
