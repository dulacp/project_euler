#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 077
#

from decorators import benchmark
from prime import *

N = 5000

@benchmark
def solve():
  """
  http://mathworld.wolfram.com/PartitionFunctionP.html
  """
  def graph(coins, amount, partial_sum=0):
    count = 0
    for i,c in enumerate(coins):
      if c > amount:
        continue
      elif c == amount: 
        count += 1
      else: 
        partial_sum += c
        count += graph(coins[i:], amount-c, partial_sum)
    return count
  n = 1
  P = Prime([2,3])
  while True:
    for p in P.gen(limit=n): pass
    g = graph(P, n)
    if g > N:
      break
    n += 1
  return n

if __name__ == "__main__":
  solve()