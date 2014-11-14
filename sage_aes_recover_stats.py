#!/usr/bin/env sage -python
# -*- coding: utf-8 -*-

import time
from sage.all import *

def recoverKey(n, r, c, e):
	"""n: number of rounds
		r: number of rows of the state array
		c: number of columns of the state array
		e: word size"""
	print "n:", n, "r:", r, "c:", c, "e:", e
	vectorp = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1]
	vectork = [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
	aes = mq.SR(n, r, c, e, gf2=True, star=True, allow_zero_inversions=True)
	plain = aes.vector(vectorp[0:(r*c*e)])
	print "plain:", plain._list()
	key = aes.vector(vectork[0:(r*c*e)])
	print "key:", key._list()
#	set_verbose(2)
	cipher = aes(plain, key)
#	set_verbose(0)
	print "cipher:", cipher._list()
	t0 = time.time()
	F, s = aes.polynomial_system(P=plain, C=cipher)
	print "number of solutions:", len(F.ideal().variety())
	print F.groebner_basis()
	for V in F.ideal().variety():
		tmp = []
		for key, value in sorted(V.items()):
			if str(key)[0:2] == "k0":
				tmp.append(int(value))
		result = []
		for i in range(len(tmp)):
			result.append(tmp[len(tmp)-1-i])
		print result
	print time.time() - t0
	print

if __name__ == "__main__":
	recoverKey(1, 1, 1, 4)
#	recoverKey(2, 1, 1, 4)
#	recoverKey(3, 1, 1, 4)
#	recoverKey(4, 1, 1, 4)
#	recoverKey(1, 2, 1, 4)
#	recoverKey(2, 2, 1, 4)
#	recoverKey(3, 2, 1, 4)
#	recoverKey(4, 2, 1, 4)
#	recoverKey(1, 2, 2, 4)
#	recoverKey(2, 2, 2, 4)

#	recoverKey(1, 1, 1, 8)
#	recoverKey(2, 1, 1, 8)
#	recoverKey(3, 1, 1, 8)
#	recoverKey(4, 1, 1, 8)
#	recoverKey(1, 2, 1, 8)
#	recoverKey(2, 2, 1, 8)
#	recoverKey(1, 2, 2, 8)
