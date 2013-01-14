#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 095
#
# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper 
# divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
#
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, 
# forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.
#
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#
# 12496  14288  15472  14536  14264 ( 12496  ...)
#
# Since this chain returns to its starting point, it is called an amicable chain.
#
# Find the smallest member of the longest amicable chain with no element exceeding one million.

from decorators import benchmark
from prime import *

N = 10**6

@benchmark
def solve():
  """
  Social Numbers on Wolfram

  NB: speed up the sum of divisors by using the prime factorisation
  """

  def proper_divisor_sigma(n):
    """http://www.mersennewiki.org/index.php/Aliquot_Sequences"""
    return reduce(lambda x,y: x * 1.0*(y[0]**(y[1]+1)-1)/(y[0]-1), prime_factors_opti(n), 1.0) - n

  lookup_table = {}
  def amicable_chain(n):
    n0 = n
    l = []
    while True:
      if n in lookup_table:
        n = lookup_table[n]
      else:
        t = proper_divisor_sigma(n)
        lookup_table[n] = t
        n = t
      if n in l:
        break
      l.append(n)
      if n <= 1 or n > N or n == n0:
        break
    return l

  m = (0, [])
  for i in range(1,N):
    c = amicable_chain(i)
    if c and c[-1] == i:
      #print c
      m = max(m, (len(c), c))

  return int(min(m[1])), m

@benchmark
def slow():
  """
  Social Numbers on Wolfram
  """

  def proper_divisor_sigma(n):
    return sum(k for k in xrange(1,n) if n%k==0)

  lookup_table = {}
  def amicable_chain(n):
    n0 = n
    l = []
    while True:
      if n in lookup_table:
        n = lookup_table[n]
      else:
        t = proper_divisor_sigma(n)
        lookup_table[n] = t
        n = t
      l.append(n)
      if n <= 1 or n > N or n in l or n == n0:
        break
    return l

  m = (0, [])
  for i in range(1,N):
    #print i, amicable_chain(i)
    c = amicable_chain(i)
    m = max(m, (len(c), c))

  return min(m[1]), m

if __name__ == "__main__":
  solve()
  slow()