#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 066
#
# Consider quadratic Diophantine equations of the form:
#
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 649^2 – 13x180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
# 3^2 – 2x2^2 = 1
# 2^2 – 3x1^2 = 1
# 9^2 – 5x4^2 = 1
# 5^2 – 6x2^2 = 1
# 8^2 – 7x3^2 = 1
#
# Hence, by considering minimal solutions in x for D <= 7, the largest x is obtained when D=5.
#
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

from decorators import benchmark
from fractions import Fraction
import math 

@benchmark
def solve():
  #limit = 7
  limit = 1000
  is_square = lambda x: x == math.pow(round(math.pow(x,1./2)),2)

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

  def solve_diophantine(D):
    """return minimal (x,y) for which x**2 - D*y**2 = 1

       [http://fr.wikipedia.org/wiki/M%C3%A9thode_chakravala]
    """
    cycle = infinit_square_decomp(D)
    cycles = [int(math.sqrt(D))] + cycle
    n = 0
    while True:
      r = reduce(lambda x,y: Fraction(1,x)+y, cycles[:n+1][::-1])
      if r.numerator**2 - D*r.denominator**2 == 1:
        return (r.numerator, r.denominator)
      n += 1
      if n%len(cycle)==0:
        cycles += cycle

  #sol = solve_diophantine(13)
  #print "13 sol", sol
  #raw_input()

  m = (0,0)
  for d in xrange(2,limit+1):
    if is_square(d): continue
    sol = solve_diophantine(d)
    if not sol:
      print "no sol for x^2 - %d*y^2 = 1" % d
      pass
    else:
      x,y = sol
      #print "(%d)^2 - %d*(%d)^2 = 1" % (x, d, y)
      if x > m[1]: 
        m = (d,x)
        print m
  return m

if __name__ == "__main__":
  solve()