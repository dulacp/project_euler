#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 088
#
# A natural number, N, that can be written as the sum and product of a given set of at least two natural 
# numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1  a2  ...  ak.
#
# For example, 6 = 1 + 2 + 3 = 1  2  3.
#
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
# The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#
# k=2: 4 = 2 x 2 = 2 + 2
# k=3: 6 = 1 x 2 x 3 = 1 + 2 + 3
# k=4: 8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
#
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only 
# counted once in the sum.
#
# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

from decorators import benchmark
from prime import *
from permut import *

N = 200

@benchmark
def solve():
  """
  Use a custom generating function to retrieve partition of size k
  inspired by the IntegerPartitions.mckay method
  """
  import IntegerPartitions
  from decorators import memoized
  prod = lambda iterable: reduce(lambda x,y: x*y, iterable, 1)

  def fixed_length_partitions(i,k):
    return IntegerPartitions.fixed_length_partitions(i,k)
  
  s = set()
  i = 2
  for k in range(2,N+1):
    i = k
    while True:
      factors = dict(prime_factors_opti(i))
      v = sum(f*m for f,m in factors.items()) + k - sum(factors.values())
      if v == i:
        break
      elif v < i:
        for p in fixed_length_partitions(i,k):
          if prod(p) == i: 
            break
        if prod(p) == i:
          break
      i += 1
      print i
    print "found", i, k
    s.add(i)
  return sum(s)

@benchmark
def slow():
  """
  Use a generating function to retrieve partition of size k
  and determine the smallest integer that satisfy sum(ak) = prod(ak)

  EDIT: works but two slow (exponential time to compute the partitions)
  """
  import IntegerPartitions
  prod = lambda iterable: reduce(lambda x,y: x*y, iterable, 1)

  s = set()
  i = 2
  for k in range(2,N+1):
    #i = k
    while True:
      for p in IntegerPartitions.mckay(i): 
        if len(p) != k: continue
        if prod(p) == i: 
          break
      if prod(p) == i:
        break
      i += 1
    print "found", i, k
    s.add(i)
  return sum(s)


@benchmark
def attempt():
  def is_sub_factor(s,d):
    """Check if s is a "subfactor" of d"""
    if gcd(d,s) == 1:
      return False
    fs = dict(prime_factors_opti(s))
    fd = dict(prime_factors_opti(d))
    for k in fs:
      if k not in fd or fs[k] > fd[k]:
        return False
    return True

  def combi_factors(d):
    return [i for i in range(2,d) if is_sub_factor(i,d)]

  # test
  t = 16
  print t
  print "test combi", combi_factors(t)
  raw_input("test ok ?")

  def check(d, k):
    _f = dict(prime_factors_opti(d))
    if sum(k*_f[k] for k in _f) + (k-sum(_f.values()))*1 == d:
      return True
    for c in combi_factors(d):
      fc = prime_factors_opti(c)
      f = {k:_f[k]-(fc[k] if k in fc else 0) for k in _f}
      if c + sum(k*f[k] for k in f) + (k-1-sum(f.values()))*1 == d:
        return c
    return None

  s,i = set(),2
  for k in xrange(2,N+1):
    while True:
      if not is_prime(i):
        if check(i,k) is not None:
          print k,i,check(i,k)
          raw_input()
          break
        else: 
          print "reject", k, i
          raw_input()
        # f = prime_factors_opti(i)
        # if sum(t[1]*t[0] for t in f) + (k-sum(t[1] for t in f))*1 <= i:
        #   s.add(i)
        #   print k,i
        #   break
      i += 1
  return sum(s), sorted(list(s))[-10:]

if __name__ == "__main__":
  solve()