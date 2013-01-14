#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 46
#
# It was proposed by Christian Goldbach that every odd composite number can 
# be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2 x 1^2
# 15 = 7 + 2 x 2^2
# 21 = 3 + 2 x 3^2
# 25 = 7 + 2 x 3^2
# 27 = 19 + 2 x 2^2
# 33 = 31 + 2 x 1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import time
from prime import *

t = time.time()

for odd in xrange(9,10**6,2):
  if is_prime(odd): continue
  sq,r = 1,0
  while 2*sq**2 < odd:
    temp = odd-2*sq**2
    if is_prime(temp):
      r = temp
      break
    sq += 1
  # if r > 0:
  #   print "%d = %d + 2*%d^2" % (odd, r, sq)
  if r == 0:
    print "contre exemple:", odd
    break

print "time: %f s" % (time.time() - t)