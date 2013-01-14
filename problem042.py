#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 42
#
# The nth term of the sequence of triangle numbers is given by, tn = 0.5*n*(n+1); 
# so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
#
# By converting each letter in a word to a number corresponding to its alphabetical 
# position and adding these values we form a word value. For example, the word value 
# for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we 
# shall call the word a triangle word.
#
# Using words.txt (right click and ‘Save Link/Target As…’), a 16K text file containing 
# nearly two-thousand common English words, how many are triangle words?

# PITOU
# the equation is
#
# n**2 + n - 2*tn = 0
#
# delta = 1 + 4*2*tn
# so the solution are n1 = (sqrt(1 + 8*tn) - 1)/2 and n2 = -n1

import math
import time

alpha = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_triangle(score):
  r = (math.sqrt(1 + 8*score) - 1)/2
  return int(r) == r

def score(w):
  return sum(alpha.index(l) for l in w)

t = time.time()
s = 0

with open('problem042_words.txt', 'r') as f:
  words = f.read().split(',')
  for w in words:
    w = w.strip('"')
    if is_triangle(score(w)):
      s += 1

print s
print "time: %f s" % (time.time() - t)
