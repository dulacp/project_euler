#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 097
#

from decorators import benchmark

#N = 7830457
N = 7830457
L = 10**10 # 10 last digits

@benchmark
def solve():
  d = 1
  for i in xrange(N):
    d = (d*2) % L
  return (28433*d+1) % L

@benchmark
def slow():
  return str(28433*(2 << (N-1)) + 1)[-10:]

if __name__ == "__main__":
  solve()
  slow()