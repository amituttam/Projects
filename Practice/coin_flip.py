
import random

def coin_flip(n):
    outcomes = [random.randint(0,1) for _ in range(n)]
    nheads = sum(outcomes)
    ntails = sum([1 for i in outcomes if i == 0])
    
    print("%(outcomes)s %(nheads)d,%(ntails)d" % locals())

coin_flip(100)
