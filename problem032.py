#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39  186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# very SMART
ran = xrange(0,10)
possa = [10*a + b for a in ran for b in ran if a <> b]
possb = []
for a in xrange(100,9999):
    x = str(a)
    y = set(x)
    if len(x) == len(y): possb.append(a)
sol = []
for a in possa:  
    for b in possb:
        if b < max(a,1000.0 / a): continue
        if b > 9999.0 / a: break        
        c = a*b
        if "".join(sorted(str(a)+str(b)+str(c))) == "123456789":            
            sol.append(c)
sol = set(sol)
print sum(sol)

# ME
# the notation
#
# a*b = c
# p = len(a)
# q = len(b)
# r = len(c)
#
# math considerations lead to 3.5 <= r <= 4
# so r = 4
#
# and also even/odd considerations lead to
# (c % 2 = 1) => (a % 2 = 1) and (b % 2 = 1)

r = 4
pandigitals = set()

def permut(digits=range(3)):
  sdigits = [str(d) for d in digits]
  d = sdigits[0]
  if len(sdigits) == 1:
    yield [d]
  else:
    for p in permut(sdigits[1:]):
      for i in range(len(p)+1):
        pp = list(p)
        pp.insert(i,d)
        yield ''.join(pp)

for p in permut(range(1,9+1)):
  for i in range(1,9-r):
    a,b,c = map(lambda x: int(x), (p[:i], p[i:-r], p[-r:]))
    a,b = min(a,b), max(a,b)
    if a*b == c:
      pandigitals.add(c)

#print pandigitals
print sum(pandigitals)