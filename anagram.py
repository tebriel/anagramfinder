#!/usr/local/bin/python3

import re
import itertools
import sys
import time

def build_word_list(text):
    word_reg = re.compile('[a-zA-Z]{4,}')
    return set([x.lower() for x in re.findall(word_reg, text)])

def find_anagram(word_list):
    combined_words = itertools.combinations(word_list, 2)

    unique_list = set()
    unique_sets = {}

    for word in combined_words:
        joined = ''.join(sorted("%s%s" % (word[0], word[1])))
        if joined in unique_list:
            other = unique_sets[joined]
            if not word[0] in other and not word[1] in other:
                print("%s %s, %s %s" % (other[0], other[1], word[0], word[1]))
        else:
            unique_list.add(joined)
            unique_sets[joined] = tuple([word[0], word[1]])

if __name__ == '__main__':
    start_time = time.time()
    word_list = build_word_list(sys.stdin.read())
    find_anagram(word_list)
    print(time.time() - start_time, "seconds")
