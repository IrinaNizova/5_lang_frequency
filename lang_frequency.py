from collections import Counter
import sys
import re


def load_data(filepath):
    words_dict = Counter()
    file_object = open(filepath, "r")
    lines = file_object.readlines()
    for line in lines:
        match_patterns = re.findall(r'\b\w{2,25}\b', line)
        for word in match_patterns:
            words_dict[word] += 1
    get_most_frequent_words(words_dict)


def get_most_frequent_words(words_dict):
    frequent_words_number = 10
    for word in words_dict.most_common(frequent_words_number):
        print('{} found {} times'.format(word[0], word[1]))


if __name__ == '__main__':
    load_data(sys.argv[1])
