#!/usr/bin/env python
#
# The Euler Project: problem 14
#
# The following iterative sequence is defined for the set of positive integers:
#
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13  40  20  10  5  16  8  4  2  1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def syracuse(x0):
  x = x0
  while x != 1:
    x = x/2 if x%2==0 else 3*x+1
    yield x
  yield x

def syracuse_fly(x0):
  """compute only the len of the syracuse suite"""
  count = 0
  x = x0
  while x != 1:
    x = x/2 if x%2==0 else 3*x+1
    count += 1
  return count+1


m,n = 0,0
for i in xrange(1,int(1e6)):
  mm = syracuse_fly(i)
  if mm > m:
    n = i
    m = mm
    print n, m
print "end"
