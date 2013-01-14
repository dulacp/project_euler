#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 086
#

from decorators import benchmark
from prime import gcd
from utils import is_square
import math

##
# Pitou: by unfolding the cube (a x b x c)
#
#                           ---------F
#                          |         |
#                          |         |
#         F--------- ------ --------- ---c--F
#         |         |      |         |      |
#         |         |      |         |      |
#         |         |      |         b      |
#         |         |      |         |      |
#         |         |      |         |      |
#          --------- ------S----a---- ------
#                          |         |
#                          |         |
#                           ---------
#                          |         |
#                          |         |
#                          |         |
#                          |         |
#                          |         |
#                           ---------F
#
# it is obvious that d(S,F)**2 is the min between 
#
#   a**2 + (b+c)**2
#     and
#   (a+c)**2 + b**2
#
# so the problem is reduce to a pythagore triplet problem
# where we need to find the pythagore triplet that verify x**2 + y**2 = z**2 
# with x <= M and y <= 2*M
#
# so we take a <- [1..2*M]
# and if a**2 + M**2 is a square we store the possibilities that can lead to this 
# then increase M 1 by 1


#N = 2000
N = 1e6

@benchmark
def solve():
  c,m = 0,0
  while c < N:
    m += 1
    for a in xrange(2,2*m+1):
      if is_square(a*a + m*m):
        c += (m + m + 2 - a)//2 if a > m+1 else a//2
  return m,c

if __name__ == "__main__":
  solve()