#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 40
#
# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

from permut import *
import time

# first try
# t = time.time()
# n = ""
# for c in couple(range(0,10), 6, optimized=False):
#   n += str(int(''.join(c)))

# second try
t = time.time()
n,l = "",10**6
for i in xrange(l):
  n += str(i)
  if len(n) > l:
    break

print reduce(lambda x,y: x*int(y), [n[10**i] for i in range(6+1)], 1)
print "time: %f s" % (time.time() - t)