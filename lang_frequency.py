from collections import Counter
import argparse
import re


def load_data(filepath):
    with open(filepath, "r") as file_object:
        return file_object.read()


def count_words(text):
    match_patterns = re.findall(r'\b\w{2,25}\b', text.lower())
    return Counter(match_patterns)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="write name of json file")
    text = load_data(parser.parse_args().file_name)
    frequent_words_number = 10
    words_dict = count_words(text)
    for word, counter in words_dict.most_common(frequent_words_number):
        print('{} found {} times'.format(word, counter))
