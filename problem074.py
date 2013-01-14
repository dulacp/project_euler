#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 074
#

from decorators import benchmark
import math

N = 10**6

@benchmark
def solve():

  def sum_digit_factorials(string_of_digits): 
    return reduce(lambda x,y: int(x)+math.factorial(int(y)), list(string_of_digits), 0)

  def key(d):
    return ''.join(sorted(str(d).replace('0','1')))

  # test
  # p = 1479
  # c = []
  # while p not in c:
  #   c.append(p)
  #   p = sum_digit_factorials(str(p))
  # print len(c)

  l = []
  chains_memo = {}
  for n in xrange(3,N):
    n0 = n
    k0 = key(n)
    if k0 in chains_memo:
      chain = chains_memo[k0]
    else:
      chain = []
      while n not in chain:
        chain.append(n)
        k = key(n)
        n = sum_digit_factorials(k)
        if k in chains_memo:
          chain.extend(chains_memo[k][1:])
          break
      chains_memo[k0] = chain
    if len(chain) == 60:
      l.append(n0)
  return len(l)

if __name__ == "__main__":
  solve()