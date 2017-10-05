from collections import Counter
import argparse
import re


def load_data(filepath):
    with open(filepath, "r") as file_object:
        return file_object.read()


def count_words(lines):
    match_patterns = re.findall(r'\b\w{2,25}\b', lines.lower())
    return Counter(match_patterns)


def get_most_frequent_words(words_dict):
    frequent_words_number = 10
    return words_dict.most_common(frequent_words_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="write name of json file")
    text = load_data(parser.parse_args().file_name)
    words_dict = count_words(text)
    for word in get_most_frequent_words(words_dict):
        print('{} found {} times'.format(word[0], word[1]))
