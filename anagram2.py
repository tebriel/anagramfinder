#!/usr/local/bin/python3

import re
import itertools
import sys
import time

class UniqueThing(object):
    __slots__ = ['item_hash', 'item_tuples']
    def __init__(self):
        self.item_hash = []
        self.item_tuples = []
    def add_tuple(self, word_one, word_two):
        if not word_one in self.item_hash and not word_two in self.item_hash:
            self.item_hash.extend([word_one, word_two])
            self.item_tuples.append([word_one, word_two])

def build_word_list(text):
    return set(re.findall('[a-z]{4,}', text.lower()))

def print_groups(groups):
    for key, group in groups.iteritems():
        if len(group.item_tuples) == 10:
            print(', '.join(["%s %s" % (tuple(tup)) for tup in group.item_tuples]))

def find_anagram(word_list):
    combined_words = itertools.combinations(word_list, 2)

    unique_groups = {}

    for word_one, word_two in combined_words:
        joined = ''.join(sorted("%s%s" % (word_one, word_two)))
        unique = unique_groups.get(joined)
        if not unique:
            unique = UniqueThing()
            unique_groups[joined] = unique
        unique.add_tuple(word_one, word_two)
    return unique_groups

if __name__ == '__main__':
    text = sys.stdin.read()
    start_time = time.time()
    word_list = build_word_list(text)
    print(time.time() - start_time, "seconds")
    groups = find_anagram(word_list)
    print(time.time() - start_time, "seconds")
    print_groups(groups)
    print(time.time() - start_time, "seconds")
