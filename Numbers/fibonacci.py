#!/usr/bin/env python

import sys
from functools import lru_cache

def benchmark(func):
	import time
	def wrapper(*args, **kwargs):
		t = time.clock()
		res = func(*args, **kwargs)
		print(func.__name__, time.clock()-t)
		return res
	return wrapper

@lru_cache(maxsize=64)
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n-1)

n = int(sys.argv[1])
print([fibonacci(x) for x in range(n)])
