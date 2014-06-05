#!/usr/bin/env python

import sys

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)

def factorial_loop(n):
	fact = 1
	if n<=1:
		return fact

	while n != 0:
		fact *= n
		n = n-1

	return fact

print(factorial(int(sys.argv[1])))
print(factorial_loop(int(sys.argv[1])))
