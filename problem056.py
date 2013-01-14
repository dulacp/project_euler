#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 56
#
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100100 is almost 
# unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the 
# digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b  100, what is the maximum digital sum?

import time
t = time.time()

m = 0
for a in range(100):
  for b in range(100):
    m = max(m, sum(map(lambda a: int(a), list(str(a**b)))))

print m
print "time: %f s" % (time.time() - t)