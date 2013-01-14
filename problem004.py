#!/usr/bin/env python
#
# The Euler Project: problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(x):
  return str(x) == str(x)[::-1]

n = 3
l = []
for i in xrange(10**(n-1), 10**n):
  for j in xrange(i, 10**n):
    p = i*j
    if is_palindromic(p):
      l.append(p)

print max(l)