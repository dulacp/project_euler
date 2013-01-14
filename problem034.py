#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 34
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

import math

def sum_digit_factorials(a): 
  return reduce(lambda x,y: int(x)+math.factorial(int(y)), list(str(int(a))), 0)

l = []
for i in range(3,1000000):
  if sum_digit_factorials(i) == i:
    l.append(i)

print sum(l)