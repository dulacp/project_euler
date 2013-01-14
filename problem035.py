#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 35
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

from prime import *
from permut import *

import time

def is_circular_prime(x):
  x = list(str(x))
  if len(x) == 1: 
    return True
  if filter(lambda i: int(i)%2==0, x):
    return False
  for p in circular_permut(x):
    if not is_prime(int(p)):
      return False
  return True

# test
# for p in prime(100):
#   if is_circular_prime(p):
#     print p

t = time.time()
l = [p for p in prime(1e6) if is_circular_prime(p)]
print len(l)
print "time: %f s" % (time.time() - t)
