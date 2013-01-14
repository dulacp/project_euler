#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 070
#
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number 
# of positive numbers less than or equal to n which are relatively prime to n. For example, 
# as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
# Find the value of n, 1  n  107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

from decorators import benchmark
from decorators import memoized
from prime import *

N = 10**7

@benchmark
def solve():
  primes = []
  m = (float('inf'), 1)
  for p1 in prime(math.sqrt(N/10), math.sqrt(10*N)):
    for p2 in primes:
      n = p1*p2
      if n >= N:
        break
      totient = (p1-1)*(p2-1) # since p1 and p2 are primes
      if sorted(str(n)) == sorted(str(totient)):
        m = min(m, (1.*n/totient,n))
    primes.append(p1)
  return m

@benchmark
def slow():
  P = Prime([2,3])
  Factors = {}
  def prime_factors(x, lower_bound=0):
    """Décomposition en facteurs premiers"""
    if x in Factors:
      return Factors[x]
    x0 = x
    factors = []
    for p in P.gen(limit=math.sqrt(x)+1):
      if x % p == 0:

        # optimization
        if p < smallest_prime_factor:
          return None

        i = 0
        while x%p==0:
          x /= p
          i += 1
        factors.append((p,i))
        if x in Factors:
          factors.extend(Factors[x])
          Factors[x0] = factors
          x = 1
          break
    if x != 1:
      factors.append((x,1))
    Factors[x0] = factors
    return factors

  def euler_phi(n, factors=None):
    c = 1
    if factors is None:
      while n%2 == 0:
        n /= 2
        if n%2 == 0: c *= 2
      factors = [f[0] for f in prime_factors(n)]
    return int(reduce(lambda x,f: x*(1-1./f), factors, c*n))

  m = (float('inf'), 1)
  smallest_prime_factor = 0       # smallest prime factor
  for n in xrange(2,N):
    factors = prime_factors(n, lower_bound=smallest_prime_factor)
    if factors is None: 
      continue

    factors = [f[0] for f in factors]
    e = euler_phi(n, factors) 
    if sorted(str(n)) == sorted(str(e)):
      #print "find", (n,e)
      m = min(m, (1.*n/e,n))
      #smallest_prime_factor = max(smallest_prime_factor, min(factors))

  return (m, prime_factors(m[1]))

if __name__ == "__main__":
  solve()
  #slow()