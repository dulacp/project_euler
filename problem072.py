#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 072
#
# Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is 
# called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that there are 21 elements in this set.
#
# How many elements would be contained in the set of reduced proper fractions for d  1,000,000?

from decorators import benchmark
from decorators import memoized
from prime import *
import math 

N = 10**6

# very smart people!
@benchmark
def pe0072(n=N):
  """
  1. phi(n) starts with n and is reduced by (p-1)/p for each of its prime factors
  2. when starting phi(m) for m < n and having applied 1. for all prime factors p < m, phi(m) == m iff m is prime
  3. when p is prime, all its multiples can be reduced according to 1.
  4. after 2. and 3. phi(m) contains the true value for phi(m)
  """
  res = 0
  phi = range(n+1) # 1. initial situation
  for m in xrange(2, n+1):
    if phi[m] == m:  # 2. unmodified since creation -> m is prime
      for k in xrange(m, n+1, m): # 3. reduce phi(k) for all k that are multiples of m
        phi[k] *= m-1
        phi[k] //= m
    res += phi[m]  # 4. true value for phi(m) ready
  return res

# 35 s :)
@benchmark
def solve():
  def _totient(n):
    return int(reduce(lambda x,f: x*(1-1./f[0]), prime_factors_opti(n), n))

  def totient(n):
    c = 1
    while n%2 == 0:
      n /= 2
      if n%2 == 0: c *= 2
    return c*_totient(n)

  return sum(totient(i) for i in xrange(2,N+1))

@benchmark
def slow():
  def totient(n):
    return int(reduce(lambda x,f: x*(1-1./f[0]), prime_factors(n), n))
  return 0.5*(N-1)*N - sum(i-totient(i)-1 for i in xrange(2,N+1))

if __name__ == "__main__":
  pe0072()
  solve()