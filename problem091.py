#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 091
#
# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to 
# the origin, O(0,0), to form ΔOPQ.
#
# There are exactly fourteen triangles containing a right angle that can be formed when each 
# co-ordinate lies between 0 and 2 inclusive; that is,
# 0 <= x1, y1, x2, y2 <= 2.

from decorators import benchmark
import math

N = 50

@benchmark
def solve():
  """No idea to do better..."""
  return "[result]"

@benchmark
def slow():
  # OP^2 = x1^2 + y1^2
  # OQ^2 = x2^2 + y2^2
  # PQ^2 = (x2-x1)^2 + (y2-y1)^2
  s = 0
  for x1 in range(0,N+1):
    for y1 in range(0,N+1):
      for x2 in range(0,N+1):
        for y2 in range(0,N+1):
          if x1*y2 - x2*y1 == 0:
            continue
          op2 = x1*x1 + y1*y1
          oq2 = x2*x2 + y2*y2
          pq2 = (x2-x1)**2 + (y2-y1)**2
          t = (op2, oq2, pq2)
          if sum(t) == 2*max(t):
            s += 1
            #print x1,y1,x2,y2, t, sum(t), max(t)
  return s/2

if __name__ == "__main__":
  solve()
  slow()