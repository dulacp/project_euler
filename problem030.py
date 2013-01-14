#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# after math considerations
#
# with      a = sum(ak * 10^k)
# we want   a = sum(ak^p)
#
# for p = 5
#
# condition 1. sum(ak) even if a is event
#              sum(ak) odd if a is odd
#
# condition 2. limit reached if 10^(n-1)/n > 9^p

p = 5

limit_reached = lambda n: bool(10**(n-1)/n > 9**p)

def sum_digits(a):
  return sum(int(i) for i in str(a))

def sum_pows(a):
  return sum(int(i)**p for i in str(a))

n,l = 2, []
while not limit_reached(n):
  for a in xrange(10**(n-1), 10**n):
    if a%2 == sum_digits(a)%2:
      if sum_pows(a) == a:
        l.append(a)
  n += 1

print "final n", n
print l
print sum(l)
