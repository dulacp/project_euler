#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 087
#
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
#
# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, 
# and prime fourth power?

from decorators import benchmark
from prime import *
import math

N = 50*1e6

@benchmark
def solve():
  P = Prime()
  two, three, four = [],[],[]
  for p in P.gen(limit=math.sqrt(N)):
    two.append(p**2)
    three.append(p**3)
    four.append(p**4)
  print "primes and pows loaded"

  s = set()
  for t1 in two:
    if t1 >= N: 
      break
    for t2 in three:
      if t1+t2 >= N:
        break
      for t3 in four:
        if t1+t2+t3 > N:
          break
        s.add(t1+t2+t3)

  return len(s)

if __name__ == "__main__":
  solve()