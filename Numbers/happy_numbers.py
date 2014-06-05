#!/usr/bin/env python

def happy_number(n):
    if n <= 0:
        return False

    prev_sum = []
    while True:
        digits = [int(i) for i in str(n)]
        res = sum(list(map(lambda x: x**2, digits)))

        if res == 1:
            return True
        elif res in prev_sum:
            return False
        else:
            prev_sum.append(res)
            n = res

numbers = [n for n in range(1,100) if happy_number(n)]
print(numbers)
