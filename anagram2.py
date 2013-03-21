import re
import itertools
import sys
import gc

def filter_groups(groups):
    _range = range
    _len = len
    for group in groups.values():
        if _len(group) < 20: continue
        newGroup = []
        for idx in _range(0, _len(group), 2):
            word_one = group[idx]
            word_two = group[idx + 1]
            if word_one not in newGroup and word_two not in newGroup:
                newGroup.extend([word_one, word_two])
        if _len(newGroup) == 20:
            print(', '.join(["%s %s" % (group[idx], group[idx + 1]) for idx in _range(0, 20, 2)]))
            

def find_anagram(word_list):
    _sorted = sorted
    _list = list
    unique_groups = {}
    combi = itertools.combinations(word_list, 2)


    for pair in combi:
        unique_groups.setdefault(''.join(_sorted("%s%s" % pair)), []).extend(pair)

    return unique_groups

if __name__ == '__main__':
    gc.disable()
    text = sys.stdin.read()
    word_list = set(re.findall('[a-z]{4,}', text.lower()))
    groups = find_anagram(word_list)
    filter_groups(groups)
