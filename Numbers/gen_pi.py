#!/usr/bin/env python

import sys
import math

def gen_pi(n):
	count = 0
	pi = 0

	if n < 0:
		return 0

	# Set initial values for gauss-legendre algorithm
	a = 1
	b = 1/math.sqrt(2)
	t = (1).__truediv__(4)
	p = 1
	diff = a - b
	print "diff=%f (%s)" % (diff,type(diff))
	while diff != 0:
		print "count: %d diff=%f" % (count, diff)
		a_n = (a + b) / 2
		b_n = math.sqrt(a*b)
		t_n = t - p * ((a-a_n)**2)
		p_n = 2*p 

		count += 1

		# Print out pi value so far
		pi = ((a_n + b_n)**2)/(4*t_n)
		print "pi: %f" % (pi)

		# update values
		a = a_n
		b = b_n
		t = t_n
		p = p_n
		diff = a - b

		# Check how many decimal places already

def main():
	gen_pi(1)

if __name__ == "__main__":
	main()
