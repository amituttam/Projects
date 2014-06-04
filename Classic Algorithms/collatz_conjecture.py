#!/usr/bin/env python

import sys

def find_steps(n):
    if n < 1:
        return 0

    steps = 0
    while True:
        print n,

        if n == 1:
            return steps
        elif n%2 == 0:
            n //= 2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1

def find_steps_rec(n, steps=0):
    print n,
    if n == 1:
        return steps
    if n%2 == 0:
        return find_steps_rec(n//2, steps + 1)
    else:
        return find_steps_rec(3*n+1, steps + 1)

def find_steps_rec2(n):
    steps = 0
    print n,
    if n == 1:
        return steps
    if n%2 == 0:
        return steps + find_steps_rec2(n//2)
    else:
        return steps + find_steps_rec2(3*n+1)

steps = find_steps(int(sys.argv[1]))
print "steps=",steps
steps = find_steps_rec(int(sys.argv[1]))
print "steps=",steps
steps = find_steps_rec2(int(sys.argv[1]))
print "steps=",steps
