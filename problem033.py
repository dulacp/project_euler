#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 33
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
# to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

n,d = 1,1

for i in range(11,100):
  for j in range(i+1,100):
    if i%10 == 0 and j%10 == 0: continue
    a,aa = map(lambda x: int(x), list(str(i)))
    b,bb = map(lambda x: int(x), list(str(j)[::-1]))
    if not a or not b or aa != bb: continue
    elif float(i)/j == float(a)/int(b):
      print "%s/%s = %s/%s" % (i,j,a,b)
      n *= int(i)
      d *= int(j)

print "n/d = %s/%s = %s" % (n,d, float(n)/d)