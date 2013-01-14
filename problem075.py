#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 075
#
# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided 
# right angle triangle in exactly one way, but there are many more examples.
#
#   12 cm: (3,4,5)
#   24 cm: (6,8,10)
#   30 cm: (5,12,13)
#   36 cm: (9,12,15)
#   40 cm: (8,15,17)
#   48 cm: (12,16,20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right 
# angle triangle, and other lengths allow more than one solution to be found; for example, using 
# 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
#   120 cm: (30,40,50), (20,48,52), (24,45,51)
#
# Given that L is the length of the wire, for how many values of L  1,500,000 can exactly one integer 
# sided right angle triangle be formed?
#
# Note: This problem has been changed recently, please check that you are using the right parameters.

from decorators import benchmark
import math
from collections import defaultdict
from prime import gcd

N = int(1.5*10**6)

@benchmark
def solve():
  triplets = defaultdict(set)
  for m in xrange(2,N):
    for n in xrange(1,m):
      if gcd(m,n) != 1 or (m-n)%2==0:
        continue
      # a**2 + b**2 = c**2
      a = m*m - n*n
      b = 2*m*n
      c = m*m + n*n
      L = a+b+c
      if L > N:
        break
      triplets[L].add(tuple(sorted((a,b,c))))
      k = 2
      while k*L <= N:
        triplets[k*L].add(tuple(sorted((k*a,k*b,k*c))))
        k += 1
  print "triplets found"
  return sum(1 for k in triplets if len(triplets[k]) == 1), len(triplets)

if __name__ == "__main__":
  solve()