#!/usr/bin/env python

import sys

is_vowel = lambda x: x in 'aeiou'

def pig_latin(word):
    beg = []
    end = []
    for i in range(len(word)):
        if not is_vowel(word[i]):
            end.append(word[i])
        else:
            beg.append(word[i:])
            break
    return ''.join(beg + end) + "ay"

print(pig_latin(sys.argv[1]))
