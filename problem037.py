#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 37
#
# The number 3797 has an interesting property. Being prime itself, it is possible to 
# continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
import time

from prime import *
from permut import *

t = time.time()

# marche theorie mais ne converge pas ^^
# primes = []
# for p in prime(10,10**8):
#   if not all(int(d)%2==1 for d in str(p)): continue
#   p = str(p)
#   if all(is_prime(int(p[:-i])) and is_prime(int(p[i:])) for i in range(1,len(p))):
#     primes.append(int(p))
#     if len(primes) == 12:
#       print "eleven found! break for p =", p
#       break

def fit(p):
  p = str(p)
  return all(is_prime(int(p[:-i])) and is_prime(int(p[i:])) for i in range(1,len(p)))

# test
#print len([c for c in couple(range(1,5), 4)])

primes,r = set(), [2]+range(1,10,2)
for n in range(2,10):
  for c in couple(r, n):
    for p in permut(c):
      if p[0] in ['1','9'] or p[-1] in ['1','9']: continue
      if is_prime(int(p)) and fit(int(p)):
        primes.add(int(p))
        print p, c, len(primes)
      if len(primes) == 11:
        break
    if len(primes) == 11:
      break
  if len(primes) == 11:
    print "11 found !!!"
    break

print "sum:", sum(primes)
print primes
print "time: %f s" % (time.time() - t)