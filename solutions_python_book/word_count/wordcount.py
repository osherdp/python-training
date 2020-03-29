#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
import string


# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def words_count(file_name):
    """
    Gets a file name and returns a dictionary - {word, count} - The number of times the word appear.
    :param file_name: A file name with string lines.
    """
    punctuation_lst = string.punctuation
    count_dict = {}
    with open(file_name, 'r') as f:
        lst_lines = f.readlines()
        for line in lst_lines:
            for p in punctuation_lst:
                if p in line:
                    adds_to_count_dict(p, count_dict, line.count(p))
                    line = line.replace(p, "")

            words_lst = line.split()
            for word in words_lst:
                word = word.lower()
                adds_to_count_dict(word, count_dict)
    return count_dict


def adds_to_count_dict(word, count_dict, adding_amount=1):
    """
    :param word: The word we want to add to the dictionary.
    :param count_dict: The word-count dictionary.
    :param adding_amount: How much we want to add to the word count.
    The function enlarged the counting value of a word.
    """
    if word in count_dict:
        count_dict[word] += adding_amount
    else:
        count_dict[word] = adding_amount


def print_words(file_name):
    """
    :param file_name: File name.
    The function that counts how often each word appears in the file and prints:
    word1 count1
    word2 count2
    """
    count_dict = words_count(file_name)
    lst_sorted_keys = sorted(list(count_dict.keys()))

    for key_word in lst_sorted_keys:
        print(key_word, count_dict[key_word])


def print_top(file_name):
    """
    :param file_name: File name.
    :return: The function that counts how often each word appears in the file and prints
    the 20 most repeating words in this format:  word1 count1
                                                 word2 count2
    """
    count_dict = words_count(file_name)
    punctuation_lst = string.punctuation
    for p in punctuation_lst:
        if p in count_dict:
            del count_dict[p]
    lst_most_counted_value = list(reversed(sorted(list(count_dict.values()))))[:20]
    lst_most_counted_key = []
    for key in count_dict:
        if count_dict[key] in lst_most_counted_value:
            lst_most_counted_key.append(key)
    for value in lst_most_counted_value:
        for key in lst_most_counted_key:
            if count_dict[key] == value:
                print(key, value)


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    file_name = sys.argv[2]
    if option == '--count':
        print_words(file_name)
    elif option == '--topcount':
        print_top(file_name)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
