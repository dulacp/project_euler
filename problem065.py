#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 065
#
# [http://projecteuler.net/problem=65]
#

from decorators import benchmark
from fractions import Fraction

@benchmark
def solve():
  def e_continued_frac_gen(index=10):
    coeff = lambda k: 2*divmod(k,3)[0] if k%3==0 else 1
    k = index
    r = Fraction(1,coeff(k))
    #print k, coeff(k)
    for i in xrange(k-1,1,-1):
      r = coeff(i) + 1/r
      #print "", i, coeff(i)
    return 2+1/r

  for i in range(2,101):
    p = e_continued_frac_gen(i)
    print p, float(p)
  return sum(map(int, list(str(p.numerator))))

if __name__ == "__main__":
  solve()