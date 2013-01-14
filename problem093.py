#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 093
#
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four 
# arithmetic operations (+, , *, /) and brackets/parentheses, it is possible to form different positive integer targets.
#
# For example,
#
# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3)  1
# 36 = 3 * 4 * (2 + 1)
#
# Note that concatenations of the digits, like 12 + 34, are not allowed.
#
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 
# is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
#
# Find the set of four distinct digits, a  b < c  d, for which the longest set of consecutive positive 
# integers, 1 to n, can be obtained, giving your answer as a string: abcd.


# force the division to be float
from __future__ import division

from decorators import benchmark
from permut import *

@benchmark
def solve():
  ops = ['+', '-', '*', '/']
  # NB: 2 pairs of parentheses are enough

  def consecutive_length(s):
    l = sorted(list(s))
    for i,e in enumerate(l):
      if i+1 != e:
        break
    return i


  def find(digit_set):
    s = set()
    for p in permut(digit_set):
      for c in couple(ops, length=3, optimized=False):
        l = list(p)

        # add ops
        for i,cc in enumerate(c):
          l.insert(2*i+1, cc)

        # for the first parentheses
        for i in range(int(len(l)/2)):
          for j in range(i+1, int(len(l)/2)+2):

            # for the second parentheses
            for ii in range(i):
              for jj in range(i+1, int(len(l)/2)+2):    

                # make a copy
                ll = l[:] 

                # add first parentheses
                ll.insert(2*i, '(')
                ll.insert(2*j, ')')

                # add second parentheses
                # NB: can be optimized but i don't know how... :/
                ll.insert(2*ii, '(')
                ll.insert(2*jj, ')') 

                #raw_input(ll)

                try:
                  v = eval(' '.join(ll))
                  if v > 0 and int(v) == v:
                    s.add(int(v))
                  #print ' '.join(ll), eval(' '.join(ll))
                except:
                  pass
    return s

  print "test {1,2,3,4} -> ", consecutive_length(find(range(1,4+1)))

  m = (0,())
  for c in couple(range(1,10), length=4):
    if len(set(c)) != 4:
      continue
    l = consecutive_length(find(c))
    print c, l
    m = max(m, (l, c))
  return m

if __name__ == "__main__":
  solve()