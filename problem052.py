#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 52
#
# It can be seen that the number, 125874, and its double, 251748, contain 
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import time
from permut import *

t = time.time()

p = 0
r = range(2,6+1)
for n in range(1,10):
  for i in xrange(10**(n-1), int(5./3*10**(n-1))+1):
    si = sorted(str(i))
    if all(si == sorted(str(i*m)) for m in r):
      p = i
      break
  if p:
    break

print p
print "time: %f s" % (time.time() - t)