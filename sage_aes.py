#!/usr/bin/env sage -python
# -*- coding: utf-8 -*-

from sage.all import *

def aes_128(round):
	""" AES: FIPS 197 implementation """
	aes = mq.SR(round, 4, 4, 8, star=True, allow_zero_inversions=True)
	print aes
	print aes.base_ring()
	print aes.base_ring().polynomial()
	print aes.sbox_constant()
	print
	print '#### key schedule ####'
	key = '2b7e151628aed2a6abf7158809cf4f3c'
	print 'key:', key
	temp = [aes.base_ring().fetch_int(ZZ(key[i:i+2], 16)) for i in range(0, len(key), 2)]
	key = aes.state_array(temp)
	print key
	print aes.hex_str(key)
	for r in range(aes.n):
		key = aes.key_schedule(key, r+1)
		print aes.hex_str(key)
	print
	print '#### AES ciphering process ####'
	plain = '00112233445566778899aabbccddeeff'
	key = '000102030405060708090a0b0c0d0e0f'
	set_verbose(2)
	cipher = aes(plain, key)
	set_verbose(0)

if __name__ == "__main__":
	aes_128(10)
