#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 000
#
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
# and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
# P(BB) = (15/21)(14/20) = 1/2.
#
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
# is a box containing eighty-five blue discs and thirty-five red discs.
#
# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine 
# the number of blue discs that the box would contain.

from decorators import benchmark
import math

#N = 10**12
N = 10**12

#
# Answer from OEIS A046090
#
# 1070379110497

@benchmark
def solve():
  """
  get n by a recurence formula

  a(n) = 6*a(n-1)-a(n-2)-2

  and guess b
  """
  n = 1
  nn = 4
  while n <= N:
    t = 6*nn - n - 2
    n = nn
    nn = t
  b = (1.0 + math.sqrt( 1+2*n*(n-1) ))/2
  return n,b


@benchmark
def still_slow():
  """
  Ok ^^ other approach

  B*(B-1) = 0.5*N*(N-1)

  leads to N*(N-1) % 4 == 0

  so N = 4*m
  or N = 4*m + 1
  """
  m = N/4
  n = 4*m
  B = 0
  while not B:
    n += 1
    b = (1.0 + math.sqrt( 1+2*n*(n-1) ))/2
    if int(b) == b:
      B = b
      break
    n += 3
    b = (1.0 + math.sqrt( 1+2*n*(n-1) ))/2
    if int(b) == b:
      B = b
      break
    m += 1
  return n, B

@benchmark
def slow():
  """
  the equation to solve is find B for 
  ( B*(B-1) ) / ( N*(N-1) ) = 0.5

  which leads to 
  B^2 - B - 0.5*N*(N-1) = 0

  so the resolution
  Delta = 1 + 4*0.5*N*(N-1) = 1 + 2*N*(N-1)
  b1 = (1 + sqrt(Delta))/2

  so we must have 
    - Delta a perfect square  => S exists such that : 1 + 2*N*(N-1) = S^2
    - (1 + sqrt(Delta)) even  => sqrt(Delta) is odd => S is odd

  so pick a S odd and resolve
  2*N^2 - 2*N - S^2 + 1 = 0

  DeltaN = 4 - 4*2*(1-S^2) = 4 - 8*(1-S^2)
  n1 = (2 + sqrt(DelatN))/4 = (1 + sqrt( 1-2*(1-S^2) ))/2
  """
  n = 0
  #s = int(math.sqrt(1+2*N*(N-1)))
  s = 0
  if s%2==0: s -= 1
  while n <= N:
    n1 = (1.0 + math.sqrt( 1-2*(1-s*s) ))/2
    #print n1, s, (1.-s*s)/2
    #raw_input()
    if int(n1) == n1:
      n = n1
      #print n
    s += 2

  return n, (1.0 + math.sqrt( 1+2*n*(n-1) ))/2

if __name__ == "__main__":
  solve()
  still_slow()
  slow()