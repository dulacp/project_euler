#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 071
#
# Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is 
# called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size, 
# find the numerator of the fraction immediately to the left of 3/7.

from decorators import benchmark
from fractions import Fraction

# no code version ^^
# 3/7 == 428571/999999

@benchmark
def solve():
  #N = 8
  N = 10**6
  m = (0,1)
  xinf = 0
  for d in xrange(N+1, 1, -1):
    for n in xrange(int(3.*d/7), xinf, -1):
      if 1.*n/d == 3./7: continue
      if 1.*n/d > 1.*m[0]/m[1]:
        m = (n,d)
        print m
        xinf = int(1.*m[0]/m[1])
        break
  return m,Fraction(*m)

@benchmark
def slow():
  #N = 10**3
  N = 8
  queue = set()
  f = (1,N)
  comp = lambda a: float(a[0])/a[1]

  while float(f[0])/f[1] != 3./7 and f[1] <= N:
    f1,f2,f3 = 3*[(1,1)]

    if f[0] < f[1]+1:
      f1 = (f[0]+1, f[1])
      f2 = (f[0], f[1]-1)
    if queue:
      f3 = min(queue, key=comp)

    ff = min(f1,f2,f3, key=comp)
    queue.add(f1)
    queue.add(f2)
    queue.remove(ff)

    f = ff
    print Fraction(*f)
  return "[result]"

if __name__ == "__main__":
  solve()