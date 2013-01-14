#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 094
#

from decorators import benchmark
from prime import *
import math

N = 10**9

@benchmark
def solve():
  s = 0
  for m in xrange(2,N/3+1):
    for n in xrange(1,m):
      if gcd(m,n) != 1 or (m-n)%2 == 0:
        continue
      # a**2 + b**2 = c**2
      a = m*m - n*n
      b = 2*m*n
      c = m*m + n*n
      L = 2*min(a,b) + 2*c
      if L > N:
        return s
      if abs(2*a - c) == 1 or abs(2*b - c) == 1:
        A = a*b
        if int(A) == A:
          #print min(a,b), max(a,b), c, L
          #raw_input()
          s += L
  return s

@benchmark
def slow():
  s = 0
  for i in xrange(2,N/3+1):
    for j in [-1,+1]:
      h = math.sqrt(i**2 - (1.*(i+j)/2)**2)
      a = i*h
      if int(a) != a:
        continue
      #print 1.*(i+j)/2, h, i, 2*i+(i+j)
      #raw_input()
      s += 2*i+(i+j) # add perimeter
  return s

if __name__ == "__main__":
  solve()
  slow()