#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 068
#
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
# 
# Working clockwise, and starting from the group of three with the numerically lowest external node
# (4,3,2 in this example), each solution can be described uniquely. For example, the above solution 
# can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight 
# solutions in total.
#
#   Total   Solution Set
#   9       4,2,3; 5,3,1; 6,1,2
#   9       4,3,2; 6,2,1; 5,1,3
#   10      2,3,5; 4,5,1; 6,1,3
#   10      2,5,3; 6,3,1; 4,1,5
#   11      1,4,6; 3,6,2; 5,2,4
#   11      1,6,4; 5,4,2; 3,2,6
#   12      1,5,6; 2,6,4; 3,4,5
#   12      1,6,5; 3,5,4; 2,4,6
#
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
#
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. 
# What is the maximum 16-digit string for a "magic" 5-gon ring?

from decorators import benchmark
from permut import couple

# Superbe version en python
#
# constraint = [lambda c: True] * 10
# constraint[0] = lambda c: c[0] == 10
# constraint[4] = lambda c: c[0] + c[1] == c[3] + c[4]
# constraint[6] = lambda c: c[2] + c[3] == c[5] + c[6]
# constraint[8] = lambda c: c[4] + c[5] == c[7] + c[8]
# constraint[9] = lambda c: c[6] + c[7] == c[1] + c[9]

# sides, rots = [0,1,2,3,2,4,5,4,6,7,6,8,9,8,1], []
# for i in range(0, len(sides), 3): rots.append(sides[i:] + sides[:i])

# search, sols = [[]], []
# while len(search) > 0:
#     c = search.pop()
#     left = set(range(1, 11)) - set(c)
#     if len(left) == 0: sols.append(c)
#     for cv in left:
#         if constraint[len(c)](c + [cv]): search.append(c + [cv])

# for sol in sols:
#     sol[:] = min([sol[cidx] for cidx in rot] for rot in rots)

# print reduce(lambda a, b: a + b, map(str, max(sols)))

@benchmark
def solve():
  # polygon = 3
  # first_digit = 4
  # r = filter(lambda x: x!=first_digit, range(1,7))
  polygon = 5
  first_digit = 10
  r = filter(lambda x: x!=first_digit, range(1,11))

  matchs = []
  for c in couple(r, 2, optimized=False):
    if c[0] == c[1]: continue
    c = map(int, c)
    c.insert(0, first_digit)
    glines = [[c]]
    for lines in glines:
      rr = filter(lambda x: x not in reduce(lambda x,y: x+y, lines), r)
      if len(lines) == polygon-1:
        last = [rr[0], lines[-1][-1], lines[0][1]]
        if sum(last) == sum(lines[0]):
          lines.append(last)
          matchs.append(lines[:])
          print "find", lines
          continue
      for cc in couple(rr, 2, optimized=False):
        if cc[0] == cc[1]: continue
        cc = map(int, cc)
        cc.insert(1, lines[-1][-1])
        if sum(cc) != sum(lines[0]): continue
        newlines = lines[:]
        newlines.append(cc)
        glines.append(newlines)
    
  # "sort" the lines by turning cyclicly until the first element of the first line has the minimal value
  matchs_sorted = []
  for lines in matchs:
    index = lines.index(min(lines))
    matchs_sorted.append( lines[index:] + lines[:index] )
  return max([int(''.join(map(str, reduce(lambda x,y:x+y, m)))) for m in matchs_sorted])

if __name__ == "__main__":
  solve()