#!/usr/bin/env python
#
# The Euler Project: problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for a in range(1,500):
  b = -(1e6 - 2000.*a)/(2*a - 2000)
  if b == int(b):
    c = 1000 - a - b
    print a*b*c