#!/usr/bin/env python
#
# The Euler Project: problem 15
#
# Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
# cf. image [http://projecteuler.net/project/images/p_015.gif]
#
# How many routes are there through a 2020 grid?

import numpy as np


size = 20

# Smart ^^
def factoriel(n):
  return np.arange(1,n+1, dtype=float).prod()
print int(factoriel(2*size)/(factoriel(size)**2))

# Brute...
def brute_force(size):
  class path(list):
    def next_nodes(self):
      l = []
      last = self[-1]
      if last[0] < size:
        l.append( (last[0]+1, last[1]) )
      if last[1] < size:
        l.append( (last[0], last[1]+1) )
      return l

    def done(self):
      return self and self[-1] == (size, size)

  n0 = (0,0)
  paths = [path( (n0,) )]

  while False in [p.done() for p in paths]:
    print "inter", len(paths)
    new_paths = []
    for p in paths:
      if p.done():
        continue
      nodes = p.next_nodes()
      if nodes:
        p.append(nodes[0])
      if len(nodes) > 1:
        pp = path(p[:])
        pp.append(nodes[1])
        new_paths.append(pp)
    paths.extend(new_paths)

  return len(paths)

#print brute_force(size)