#!/usr/bin/env python
#
# The Euler Project: problem 26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10  =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

# With the Fermat's little theorem
# which states that
#
# if p is a prime number then for any interger a
# a^(p-1) = 1 (mod p)
#
# particularly for a = 10
# 10^(p-1) = 1 (mod p)
#
# we can deduce that 10 is a primitive root module p
# that means that the period of 10**k module p is p-1
#
# so we need to find the greatest prime number under 1000

from prime import *
import time
import math

def find_group_of_units(a, n):
  """
  For more details check out Wiki!

  http://en.wikipedia.org/wiki/Order_(number_theory)
  """
  group, i = [], 1
  amodn = a
  while amodn != 1:
    amodn = (amodn*a) % n
    group.append(amodn)
    i += 1
  group.append(amodn)
  return group

#test
# test = [1, 3, 5, 9, 11, 13]
# for t in test:
#   print t, find_group_of_units(t, 14)

t_start = time.time()

d, group_of_units = 7, find_group_of_units(10, 7)
for p in prime(1000):
  if p > d:
    new_group_of_units = find_group_of_units(10, p)
    if len(new_group_of_units) > len(group_of_units):
      d = p
      group_of_units = new_group_of_units
    #print "d=%d (group of units #%d)" % (p, len(new_group_of_units))

t_end = time.time()

print "\nMAX"
print "d = %d (group of units #%d)" % (d, len(group_of_units))
print "time : %f sec" % (t_end - t_start)
