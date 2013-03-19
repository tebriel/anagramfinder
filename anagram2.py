import re
import itertools
import sys
import gc

def filter_groups(groups):
    for group in groups.itervalues():
        if len(group) < 20: continue
        newGroup = []
        for idx in range(0, len(group), 2):
            word_one = group[idx]
            word_two = group[idx + 1]
            if word_one not in newGroup and word_two not in newGroup:
                newGroup.extend([word_one, word_two])
        if len(newGroup) == 20:
            print(', '.join(["%s %s" % (group[idx], group[idx + 1]) for idx in range(0, 20, 2)]))
            

def find_anagram(word_list):
    unique_groups = {}

    for word_one, word_two in itertools.combinations(word_list, 2):
        joined = ''.join(sorted("%s%s" % (word_one, word_two)))
        unique = unique_groups.setdefault(joined, [])
        unique.extend([word_one, word_two])

    return unique_groups

if __name__ == '__main__':
    gc.disable()
    text = sys.stdin.read()
    word_list = set(re.findall('[a-z]{4,}', text.lower()))
    groups = find_anagram(word_list)
    filter_groups(groups)
