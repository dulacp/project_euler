#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 073
#
# Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, 
# it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 3 fractions between 1/3 and 1/2.
#
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d  12,000?
#
# Note: The upper limit has been changed recently.

from decorators import benchmark

N = 12000

@benchmark
def solve():
  def farey(n, asc=True):
    """Farey sequence generator"""
    if asc:
      a,b,c,d = 0, 1, 1, n
    else:
      a,b,c,d = 1, 1, n-1, n
    yield (a,b)
    while (asc and c <=n) or (not asc and a > 0):
      k = int((n+b)/d)
      a,b,c,d = c, d, k*c-a, k*d-b
      yield (a,b)

  s = 0
  for f in farey(N):
    t = 1.*f[0]/f[1]
    if t >= 1./2:
      break
    elif 1.*f[0]/f[1] > 1./3:
      s += 1

  return s

if __name__ == "__main__":
  solve()