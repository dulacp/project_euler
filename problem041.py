#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

# math considerations
#
# 1+2+3+4+5+6+7+8+9 = 45 which is divisible by 3 so n <> 9
# 1+2+3+4+5+6+7+8 = 36 so n <> 8
# 1+2+3+4+5+6 = 21 so n <> 6
# 1+2+3+4+5 = 15 so n <> 5
# 1+2+3 = 6 so n <> 3
# 1+2 = 3 so n <> 2

import time
from permut import *
from prime import *

def is_pandigital(x):
  return ''.join(sorted(str(x))) == "123456789"

t = time.time()

m = 0
for n in [7,4]:
  for p in permut(range(n,0,-1)):
    if is_prime(int(p)):
      m = max(m, p)
  if m:
    break

print m
print "time: %f s" % (time.time() - t)