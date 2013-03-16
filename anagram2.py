#!/usr/local/bin/python3

import re
import itertools
import sys
import time

class UniqueThing:
    def __init__(self):
        self.item_hash = {}
        self.item_tuples = []
    def add_tuple(self, word_tuple):
        if not self.item_hash.get(word_tuple[0]) and not self.item_hash.get(word_tuple[1]):
            self.item_hash[word_tuple[0]] = True
            self.item_hash[word_tuple[1]] = True
            self.item_tuples.append(word_tuple)

def build_word_list(text):
    word_reg = re.compile('[a-zA-Z]{4,}')
    return set([x.lower() for x in re.findall(word_reg, text)])

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

    for word in combined_words:
        joined = ''.join(sorted("%s%s" % (word[0], word[1])))
        if not joined in unique_groups:
            unique_groups[joined] = UniqueThing()
        unique_groups[joined].add_tuple(tuple([word[0], word[1]]))

    return unique_groups

if __name__ == '__main__':
    start_time = time.time()
    word_list = build_word_list(sys.stdin.read())
    groups = find_anagram(word_list)
    print_groups(groups, 10)
    print(time.time() - start_time, "seconds")
