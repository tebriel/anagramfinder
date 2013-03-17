#!/usr/local/bin/python3

import re
import itertools
import sys
import time

class UniqueThing(object):
    __slots__ = ['item_hash', 'item_tuples']
    def __init__(self):
        self.item_hash = {}
        self.item_tuples = []
    def add_tuple(self, word_one, word_two):
        if not self.item_hash.get(word_one) and not self.item_hash.get(word_two):
            self.item_hash[word_one] = True
            self.item_hash[word_two] = True
            self.item_tuples.append(tuple([word_one, word_two]))

def build_word_list(text):
    return set(re.findall('[a-z]{4,}', text.lower()))

def print_groups(groups, count):
    for key in groups:
        if len(groups[key].item_tuples) == count:
            compiled = []
            for tup in groups[key].item_tuples:
                compiled.append("%s %s" % tup)
            print(', '.join(compiled))

def find_anagram(word_list):
    combined_words = itertools.combinations(word_list, 2)

    unique_groups = {}

    for word_one, word_two in combined_words:
        joined = ''.join(sorted("%s%s" % (word_one, word_two)))
        if not unique_groups.get(joined):
            unique_groups[joined] = UniqueThing()
        unique_groups[joined].add_tuple(word_one, word_two)

    return unique_groups

if __name__ == '__main__':
    text = sys.stdin.read()
    start_time = time.time()
    word_list = build_word_list(text)
    print(time.time() - start_time, "seconds")
    groups = find_anagram(word_list)
    print(time.time() - start_time, "seconds")
    print_groups(groups, 10)
    print(time.time() - start_time, "seconds")
