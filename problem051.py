#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 51
#
# By replacing the 1st digit of *3, it turns out that six of the nine possible 
# values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit 
# number is the first example having seven primes among the ten generated numbers, 
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime 
# with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
# with the same digit, is part of an eight prime value family.

import time
from collections import defaultdict
from permut import *
from prime import *

t = time.time()

def smarter():
  """
  Generate all the primes and check for a format with masks
  """
  bound =  8
  r = map(str, range(10))
  def mask(x):
    l = []
    _x = str(x)
    for i in r:
      x = list(_x)
      if x.count(i) > 1:
        index,ll = 0, []
        for k in range(x.count(i)):
          index = x.index(i,index)
          ll.append(index)
          index += 1

        # couples uniques (optimisation)
        couples = []
        for c in couple(ll, len(ll)):
          c = sorted(list(set(c)))
          if c not in couples:
            couples.append(c)
        
        # generate masks (ex. 56**3 is a mask)
        for c in couples:
          x = list(_x)
          for cc in c:
            x[int(cc)] = '*'
          l.append(''.join(x))
    return l

  #print mask(10032208)  
  #raw_input()

  masks = defaultdict(list)
  P = Prime([2,3])
  the_prime = 0
  for p in P.gen(limit=1e6):
    for m in mask(p):
      masks[m].append(p)
      if len(masks[m]) == bound:
        the_prime = masks[m][0]
        break
    if the_prime:
      break
  return the_prime

# run in 147 sec :$
def first():
  bound,the_prime = 8, float('inf')
  for n in range(6,7):
    couples = []
    for c in couple(range(n), n-1):
      c = sorted(list(set(c)))
      if c not in couples:
        couples.append(c)

    for c in couples:
      for a in range(1,10**(n-len(c))):
        primes = []
        for i in range(10):
          p = list(str(a))
          for cc in c:
            p.insert(int(cc), str(i))
          p = int(''.join(p))
          if len(str(p)) != n:
            continue
          if is_prime(p):
            primes.append(p)
        if len(primes) == bound:
          the_prime = min(the_prime, primes[0])
          print "find", the_prime
  return the_prime

#print first()
print smarter()
print "time: %f s" % (time.time() - t)