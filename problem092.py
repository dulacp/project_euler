#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 092
#
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 -> 32 -> 13 -> 10 -> 1 -> 1
# 85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

from decorators import benchmark

N = 10**7

@benchmark
def solve():
  memoiz = {}
  def chain_ending(n):
    if n == 1 or n == 89:
      return n
    k = tuple(sorted(str(n).replace('0','')))
    if k in memoiz:
      return memoiz[k]
    memoiz[k] = chain_ending(reduce(lambda x,y: x+int(y)**2, k, 0))
    return memoiz[k]

  return sum(1 for i in xrange(1,N) if chain_ending(i) == 89)

@benchmark
def slow():
  memoiz = {}
  def chain_ending(n):
    k0 = tuple(sorted(str(n)))
    while n != 1 and n != 89:
      k = tuple(sorted(str(n)))
      if k in memoiz:
        return memoiz[k]
      n = reduce(lambda x,y: x+int(y)**2, k, 0)
    memoiz[k0] = n
    return n

  return sum(1 for i in xrange(1,N) if chain_ending(i) == 89)

if __name__ == "__main__":
  solve()
  slow()