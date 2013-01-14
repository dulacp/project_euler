#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 062
#
# The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

from decorators import benchmark
from collections import defaultdict
from permut import *
import math

@benchmark
def solve():
  size,i = 5, 345
  masks = defaultdict(list)
  while True:
    c = i**3
    d = ''.join(sorted(str(c)))
    masks[d].append(c)
    if len(masks[d]) == size:
      return min(masks[d])
    i += 1
  return "[result]"

@benchmark
def low():
  cube_limit = 10000
  cubes = [i**3 for i in xrange(345,cube_limit)]
  print "cubes loaded until %d**3" % (cube_limit-1)

  for c in cubes:
    d = sorted(str(c))
    l = [c]
    for cc in cubes:
      dd = sorted(str(cc))
      if c != cc and d == dd:
        l.append(cc)
      if len(l) == 5:
        return l

  return "[result]"

@benchmark
def brute_force():
  is_cube = lambda x: x == math.pow(round(math.pow(x,1./3)),3)
  n = 5

  cube_roots = []
  for i in xrange(342,10000):
    if i in cube_roots: 
      print "already checked", i 
      continue
    l = []
    cube = i**3
    print "\n%d" % i
    for p in permut(list(str(cube))):
      p = int(p)
      if p < 41063625: continue
      if is_cube(p) and p not in l:
        l.append(p)
        cube_roots.append(round(p**(1./3)))
        print p,
      if len(l) == n:
        return min(l)

  return "[result]"

if __name__ == "__main__":
  solve()