import re
import itertools
import sys
import gc
#import time

def build_word_list(text):
    return set(re.findall('[a-z]{4,}', text.lower()))

def print_groups(groups):
    for key in groups:
        group = groups[key]
        if len(group) == 20:
            result = []
            for idx in range(0, 20, 2):
                result.append("%s %s" % (group[idx], group[idx + 1]))

            #["%s %s" % (tuple(tup)) for tup in group.item_tuples by two]
            print(', '.join(result))#))

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
    #start_time = time.time()
    word_list = build_word_list(text)
    groups = find_anagram(word_list)
    print_groups(groups)
    #print(time.time() - start_time, "seconds")
