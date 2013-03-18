import re
import itertools
import sys
import collections

class UniqueThing(object):
    __slots__ = ['item_hash', 'item_tuples']
    def __init__(self):
        self.item_hash = []
        self.item_tuples = []
    def add_tuple(self, word_one, word_two):
        if not word_one in self.item_hash and not word_two in self.item_hash:
            both = [word_one, word_two]
            self.item_hash.extend(both)
            self.item_tuples.append(both)

def build_word_list(text):
    return set(re.findall('[a-z]{4,}', text.lower()))

def print_groups(groups):
    for key, group in groups.iteritems():
        if len(group.item_tuples) == 10:
            print(', '.join(["%s %s" % (tuple(tup)) for tup in group.item_tuples]))

def find_anagram(word_list):
    unique_groups = collections.defaultdict(UniqueThing)

    for word_one, word_two in itertools.combinations(word_list, 2):
        joined = ''.join(sorted("%s%s" % (word_one, word_two)))
        unique_groups[joined].add_tuple(word_one, word_two)

    return unique_groups

if __name__ == '__main__':
    text = sys.stdin.read()
    word_list = build_word_list(text)
    groups = find_anagram(word_list)
    print_groups(groups)
