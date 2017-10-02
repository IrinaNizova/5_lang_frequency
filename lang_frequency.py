from collections import Counter
import sys
import re

words_dict = Counter()

def load_data(filepath):
    file_object = open(filepath, "r")
    lines = file_object.readlines()
    for line in lines:
        match_patterns = re.findall(r'\b\w{2,25}\b', line)
        for word in match_patterns:
            words_dict[word] += 1
    get_most_frequent_words(words_dict)


def get_most_frequent_words(words_dict):
    for word in words_dict.most_common(10):
        print('{} found {} times'.format(word[0], word[1]))


if __name__ == '__main__':
    load_data(sys.argv[1])
