#!/usr/bin/env python
#
# The Euler Project: problem 5
#
# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

t = time.time()

x = 2520
while not all([x%i==0 for i in range(11,20+1)]):
  x += 2520

print x
print "time: %f s" % (time.time() - t)