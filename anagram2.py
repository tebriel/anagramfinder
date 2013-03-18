import re
import itertools
import sys
import gc

def print_groups(groups):
    for key in groups:
        group = groups[key]
        if len(group) == 20:
            print(', '.join(["%s %s" % (group[idx], group[idx + 1]) for idx in range(0, 20, 2)]))

def find_anagram(word_list):
    unique_groups = {}

    for word_one, word_two in itertools.combinations(word_list, 2):
        joined = ''.join(sorted("%s%s" % (word_one, word_two)))
        unique = unique_groups.setdefault(joined, list())
        if not word_one in unique and not word_two in unique:
            unique.extend([word_one, word_two])

    return unique_groups

if __name__ == '__main__':
    gc.disable()
    text = sys.stdin.read()
    word_list = set(re.findall('[a-z]{4,}', text.lower()))
    groups = find_anagram(word_list)
    print_groups(groups)
