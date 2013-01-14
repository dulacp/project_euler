#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 50
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import time
from prime import *

t = time.time()

limit = 10**3
P = Prime([2,3])
for p in P.gen(limit=limit):
  pass
print "primes loaded"

def fast():
  m = 0
  _S = sum(P)
  for l in range(len(P),1,-1):
    S = _S
    S -= sum(P[l:])
    for i in range(len(P)-l):
      if S > limit:
        break
      if is_prime(S):
        m = S
      S -= P[i]
      S += P[l+i]
    if m > 0:
      break
  return m

m = fast()

print m
print "time: %f s" % (time.time() - t)
