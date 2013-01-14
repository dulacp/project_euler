#!/usr/bin/env python
#
# The Euler Project: problem 23
#
# A perfect number is a number for which the sum of its proper divisors is exactly 
# equal to the number. For example, the sum of the proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
# that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
# it can be shown that all integers greater than 28123 can be written as the sum of two 
# abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of 
# two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
import numpy as np

# original version
def _d(n):
    for i in xrange(1,n):
      if n%i == 0:
        yield i

def _sd(n):
  return sum(i for i in _d(n))

def _abundant(n):
  return _sd(n) > n

# optimized version
def d(n):
  yield 1
  comp = []
  for i in xrange(2,int(math.sqrt(n))+1):
    if n%i == 0:
      if n/i != i: # avoid to return the same divisor (for perfect square like 4, 16, 64, 256, 1024, ...)
        comp.append(n/i)
      yield i
  comp.reverse()
  for c in comp:
    yield c

def sd(n):
  return sum(x for x in d(n))

def abundant(n):
  return sd(n) > n

# convergence impossible
def brute_force():
  abundants = np.array([i for i in range(1,28123) if abundant(i)])
  print len(abundants)

  cant = []
  a = np.zeros(len(abundants))
  for i in xrange(1, 28123):
    sub = a*0 + i - abundants
    for s in sub:
      if s in abundants:
        break
    else:
      cant.append(i)
    print cant

  print cant

# smart but little brute force ^^
def smarter():
  abundants = np.array([i for i in range(1,28123) if abundant(i)])
  print len(abundants)

  cant = []
  for i in xrange(1, 28123):
    flag = True
    for a in abundants:
      if a > i/2:
        flag = True
        break
      sub = i - a
      if sub in abundants:
        flag = False
        break
    if flag:
      print i
      cant.append(i)
  print sum(cant)

# smart (less than 1 minute to compute)
def smart():
  abundants = np.array([i for i in range(1,28123) if abundant(i)])
  n = len(abundants)
  print n

  cans = set([])
  for i in xrange(n):
    xi, can = abundants[i], []
    for j in xrange(i,n):
      xj = xi+abundants[j]
      if xj > 28123:
        break
      else:
        can.append(xj)
    # prevlen = len(cans)
    cans = cans.union(can)
    # if prevlen + len(can) != len(cans):
    #   print "doublons enleves pour xi=", xi, prevlen+len(can)-len(cans), prevlen, len(can), len(cans)
  print len(cans), sum(cans)
  print np.arange(1,28123+1).sum() - sum(cans)

smart()