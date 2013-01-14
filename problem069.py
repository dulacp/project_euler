#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 069
#
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine 
# the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
# are all less than nine and relatively prime to nine, φ(9)=6.
#
#   n   Relatively Prime  φ(n)  n/φ(n)
#   2   1                 1     2
#   3   1,2               2     1.5
#   4   1,3               2     2
#   5   1,2,3,4           4     1.25
#   6   1,5               2     3
#   7   1,2,3,4,5,6       6     1.1666...
#   8   1,3,5,7           4     2
#   9   1,2,4,5,7,8       6     1.5
#   10  1,3,7,9           4     2.5
#
# It can be seen that n=6 produces a maximum n/φ(n) for n  10.
#
# Find the value of n  1,000,000 for which n/φ(n) is a maximum.

from decorators import benchmark
from prime import *

# Smart solution and fast
#
# MAX = 10 ** 6
# primes_ = primes(20)
# number, idx = 1, 0
# while number < MAX:
#   number *= primes_[idx]
#   idx += 1
#
# print number / primes_[idx-1]

@benchmark
def solve():
  P = Prime([2,3])
  Factors = {}
  def prime_factors(x):
    """Décomposition en facteurs premiers"""
    if x in Factors:
      return Factors[x]
    x0 = x
    factors = []
    for p in P.gen(limit=math.sqrt(x)+1):
      if x % p == 0:
        i = 0
        while x%p==0:
          x /= p
          i += 1
        factors.append((p,i))
        if x in Factors:
          factors.extend(Factors[x])
          x = 1
          break
    if x != 1:
      factors.append((x,1))
    Factors[x0] = factors
    return factors

  def euler_phi(n):
    factors = prime_factors(n)
    return reduce(lambda x,f: x*(1-1./f[0]), factors, n)

  return max((1.*i/euler_phi(i),i) for i in xrange(2,int(1e6)+1))

if __name__ == "__main__":
  solve()