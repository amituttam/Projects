#!/usr/bin/env python

import random

def flip_coin(n):
    nheads = 0
    ntails = 0
    
    outcomes = [1 if random.random() >=0.5 else 0 for _ in range(n)]
    nheads = sum(outcomes)
    ntails = len(outcomes) - nheads

    print "outcomes: %s (%d/%d)" % (outcomes, nheads, ntails)

flip_coin(100)
