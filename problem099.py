#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 099
#

from decorators import benchmark
import math

@benchmark
def solve():
  i,m = 0, (0,0)
  with open('problem099_base_exp.txt') as f:
    for l in f:
      a = map(int, l.strip().split(','))
      m = max(m, (a[1]*math.log(a[0]), i))
      i += 1
  return m[1]+1

if __name__ == "__main__":
  solve()