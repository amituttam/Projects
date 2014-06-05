#!/usr/bin/env python

import decimal
import sys

def legendre():
	D = decimal.Decimal
	# Create copy of the current context
	with decimal.localcontext() as ctx:
		# Increase precision by 2
		ctx.prec += 2
		a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1
		pi = None
		while 1:
			a_n = (a+b)/2
			b = (a*b).sqrt()
			t -= p * (a - a_n) * (a - a_n)
			a, p = a_n, 2*p
			piold = pi
			pi = (a+b) * (a+b) / (4*t)
			if pi == piold:
				break
	# Round final result back to default precision
	return +pi

n = int(sys.argv[1])
decimal.getcontext().prec = n+1
print(legendre())
