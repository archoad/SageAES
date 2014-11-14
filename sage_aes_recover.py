#!/usr/bin/env sage -python
# -*- coding: utf-8 -*-

import time
from sage.all import *

def recoverKey():
	aes = mq.SR(1, 1, 1, 8, gf2=True, star=True, allow_zero_inversions=True)
	plain = aes.vector([0, 1, 1, 0, 0, 1, 0, 1])
	print "plain:", plain._list()
	key = aes.vector([1, 1, 0, 0, 0, 1, 1, 1])
	print "key:", key._list()
	set_verbose(2)
	cipher = aes(plain, key)
	set_verbose(0)
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

if __name__ == "__main__":
	recoverKey()
