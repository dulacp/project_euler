#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Helpers for prime numbers
"""

import math

def is_prime(x):
  if x == 1:
    return False
  if x == 2 or x == 3:
    return True
  if x%2==0 or x%3==0:
    return False
  for i in xrange(4,int(math.sqrt(x))+1):
    if x%i == 0:
      #print "%d divise %d" % (i,x)
      return False
  return True

def prime(start=2, limit=-1):
  if limit == -1: 
    limit = start
    start = 2
  if start <= 2:
    yield 2
  i = start+1 if start%2==0 else start
  while i < limit:
    if is_prime(i):
      yield i
    i += 2 # only odd number can be prime numbers

class Prime(list):
  """
  Prime generator class with memoization!
  """
  def __init__(self, l=None):
    super(Prime,self).__init__(l if l else [2,3])

  def __getitem__(self, index):
    if index >= len(self):
      for p in prime(list.__getitem__(self,-1)+1, float('inf')):
        self.append(p)
        if index < len(self):
          break
    return list.__getitem__(self,index)
  
  def gen(self, index_limit=float('inf'), limit=float('inf')):
    i = 0
    while i < index_limit:
      v = self[i]
      if v >= limit:
        break
      yield v
      i += 1

def prime_factors(x):
  """Décomposition en facteurs premiers"""
  if x in Factors:
    return Factors[x]
  factors = []
  for p in prime(math.sqrt(x)+1):
    if x % p == 0:
      i = 0
      while x%p==0:
        x /= p
        i += 1
      factors.append((p,i))
  if x != 1:
    factors.append((x,1))
  return factors

Factors = {}
P = Prime([2,3])
def prime_factors_opti(x):
  """Décomposition en facteurs premiers avec memoization"""
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

def gcd(a,b):
  while b != 0:
     t = b
     b = a % b
     a = t
  return a

def d(n):
  return reduce(lambda x,y: x+(1+y[1]), prime_factors(n), 0) - 2

def divisors(n):
  return (k for k in range(1,n+1) if n%k==0)

def divisors_sigma(n, k=1):
  if k == 1: return sum(divisors(n))
  return sum(i**k for i in divisors(n))
