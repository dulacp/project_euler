#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 064
#
# [http://projecteuler.net/problem=64]
#

from decorators import benchmark
from fractions import Fraction
import math

@benchmark
def solve():
  is_square = lambda x: x == math.pow(round(math.pow(x,1./2)),2)
  limit = 10000

  def infinit_square_decomp(i):
    e = int(math.floor(math.sqrt(i)))
    r = e
    x = (1, r) # stands for 1./(sqrt(i)-e)
    l,frac_mem = [],[]
    while x not in frac_mem:
      frac_mem.append(x)
      simplified = Fraction(x[0], i-x[1]**2)
      ee = int((math.floor(math.sqrt(i)) + x[1])/simplified.denominator)
      rr = int(ee*simplified.denominator - x[1])
      x = (simplified.denominator, rr)
      l.append(ee)
    return l

  return sum(1 for i in xrange(2,limit+1) if not is_square(i) and len(infinit_square_decomp(i))%2==1)

if __name__ == "__main__":
  solve()