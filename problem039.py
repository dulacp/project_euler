#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 39
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

import math
import time

t = time.time()

m,mp = 0,0

for p in range(3,1000):
  i = 0
  for a in range(1,p/2):
    for c in range(a,p/2):
      b = math.sqrt(c**2-a**2)
      if a < b and b < c and int(b) == b:
        b = int(b)
        if a+b+c == p:
          i += 1
  if i > m:
    m = i
    mp = p
    print mp, m

print mp
print m
print "time: %f s" % (time.time() - t)