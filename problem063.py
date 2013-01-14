#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 063
#
# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, 
# is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

from decorators import benchmark
import math

@benchmark
def solve():
  #dlen = lambda x: math.ceil(math.log(x)/math.log(10))
  dlen = lambda x: len(str(x))
  s,n = 0,1
  while True:
    for i in range(1,10):
      if dlen(i**n) == n:
        #print i**n
        s += 1
    if dlen(i**n) < n:
      break
    n += 1
  return s

if __name__ == "__main__":
  solve()