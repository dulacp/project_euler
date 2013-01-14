#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 27
#
# Euler published the remarkable quadratic formula:
#
# n² + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 40² + 40 + 41 = 40(40 + 1) + 41 is 
# divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
#
# Using computers, the incredible formula n² − 79n + 1601 was discovered, which 
# produces 80 primes for the consecutive values n = 0 to 79. The product of the 
# coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n² + an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that 
# produces the maximum number of primes for consecutive values of n, starting with n = 0.

from prime import *

limit = 1000

couple = (0,0,[])

# simple math analysis show that a and b have to be odd togethers
# that's why we set the step to 2
for a in xrange(-limit-1,limit,2):
  for b in xrange(-limit-1,limit,2):
    primes = []
    for n in range(80):
      p = n**2 + a*n + b
      if p > 0 and is_prime(p):
        primes.append(p)
      else:
        break
    if len(primes) > len(couple[2]):
      couple = (a,b,primes)

print "(a,b,#primes) = (%d,%d,%d)" % (couple[0], couple[1], len(couple[2]))
print "product a*b =", couple[0]*couple[1]
