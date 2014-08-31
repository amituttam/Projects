#!/usr/bin/env python

def is_pal(string):
    if len(string) <= 1:
        return True
    else:
        return (string[0] == string[-1]) and is_pal(string[1:-1])

pal = lambda x: x == x[::-1]

print is_pal('racecar'), pal('racecar')
print is_pal('test'), pal('test')
print is_pal('kayak'), pal('kayak')
