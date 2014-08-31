#!/usr/bin/env python

def count_vowels(word):
    is_vowel = lambda x: x in 'aeiou'
    vowels = dict([(i,0) for i in 'aeiou'])
    for letter in word:
        if is_vowel(letter):
            vowels[letter] += 1

    print vowels,sum(vowels.values())

count_vowels('aeiou')
count_vowels('wassup')
count_vowels('hello')
count_vowels('ttrrsdsd')
