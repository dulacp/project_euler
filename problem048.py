#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 48
#
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time

# one liner
t = time.time()
print str(sum(i**i for i in range(1,1001)))[-10:]
print "time: %f s" % (time.time() - t)

# try to speed up
t = time.time()
s,l = 0, 10**10
for i in range(1,1001):
  s += (i**i) % l
print str(s)[-10:]
print "time: %f s" % (time.time() - t)