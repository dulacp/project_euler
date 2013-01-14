#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 36
#
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import math
import time

def is_palindromic(x):
  return str(x) == str(x)[::-1]

def dec2bin(x):
  x,b = int(x),''
  while x > 0:
    b += str(x % 2)
    x /= 2
  return int(b[::-1]) # convert to int to avoid leading zeros

# test
#print dec2bin(2)

t = time.time()

l = [p for p in xrange(1,10**6) if is_palindromic(p) and is_palindromic(dec2bin(p))]
print sum(l)
#print l
#print [dec2bin(p) for p in l]
print "time: %f s" % (time.time() - t)