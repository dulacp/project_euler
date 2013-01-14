#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 060
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating 
# them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 
# 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four 
# primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from decorators import benchmark
from prime import *
from collections import defaultdict
from collections import Counter

class Node:
  def __init__(self, value=0, parent=None, children=None):
    self.value = value
    self.parent = parent
    self.children = children or []

  def __str__(self):
    return str(self.parent) + " -> %d" % self.value

  def steps(self):
    if self.parent is None:
      return 0
    return self.parent.steps() + 1

  def sum(self):
    if self.parent is None:
      return self.value
    return self.parent.sum() + self.value

@benchmark
def solve():
  root = Node(0)
  for p in prime(10000):
    root.children.append(Node(p, parent=root))
  print "primes loaded"

  def walk_graph(node):
    for i in range(len(node.children)):
      ci = node.children[i]
      si = str(ci.value)
      for j in range(i,len(node.children)):
        cj = node.children[j]
        sj = str(cj.value)
        if ci.value < cj.value and is_prime(int(si+sj)) and is_prime(int(sj+si)):
          ci.children.append(Node(cj.value, parent=ci))
      if ci.steps() < 5:
        if len(ci.children) and len(ci.children) >= 5-ci.steps():
          walk_graph(ci)
      else:
        print ci.sum(), ci
        return ci.sum()

  return walk_graph(root)

@benchmark
def optimization_try():
  primes = [673,109,7,3]
  for i in xrange(673,int(1e9),1000):
    # divibilité par 3
    ps = str(i)
    digits = map(int,list(ps))
    sd = sum(digits)
    if sd%3==2: 
      #print "divible par 3 pour i", i
      continue

    # divibilité par 7
    if i%7==6:
      #print "*3 divible par 7 pour i", i
      continue
    if (2*i)%7==1:
      #print "*109 divisible par 7 pour i", i
      continue
    if i%7==1:
      #print "*673 divisible par 7 pour i", i
      continue

    # divibilité par 13
    if i%13==1:
      #print "*3 divisible par 13 pour i", i
      continue
    if i%13==11:
      #print "*7 divisible par 13 pour i", i
      continue
    if (3*i)%13==2:
      #print "*109 divisible par 13 pour i", i
      continue
    if (3*i)%13==4:
      #print "*673 divisible par 13 pour i", i
      continue

    # divibilité par 17
    if i%17==15:
      #print "*3 divisible par 17 pour i", i
      continue
    if i%17==16:
      #print "*7 divisible par 17 pour i", i
      continue
    if (15*i)%17==1:
      #print "*109 divisible par 17 pour i", i
      continue
    if (15*i)%17==16:
      #print "*673 divisible par 17 pour i", i
      continue

    # divibilité par 19
    if i%19==13:
      #print "*3 divisible par 19 pour i", i
      continue
    if i%19==5:
      #print "*7 divisible par 19 pour i", i
      continue
    if i%19==2:
      #print "*109 divisible par 19 pour i", i
      continue
    if (5*i)%19==3:
      #print "*673 divisible par 19 pour i", i
      continue

    # divibilité par 23
    if i%23==2:
      #print "*3 divisible par 23 pour i", i
      continue
    if i%23==20:
      #print "*7 divisible par 23 pour i", i
      continue
    if (8*i)%23==19:
      #print "*109 divisible par 23 pour i", i
      continue
    if (2*i)%23==1:
      #print "*673 divisible par 23 pour i", i
      continue

    # divibilité par 11
    if len(digits)%2==0:
      sd_diff = sum(digits[1::2]) - sum(digits[::2])
      if sd_diff%11!=5 or sd_diff%11!=6:
        #print "divisible par 11 pour i", i
        continue

    if not is_prime(i):
      continue
    for pp in primes:
      pps = str(pp)
      if not is_prime(int(pps+ps)):
        break
      if not is_prime(int(ps+pps)):
        break
      if pps != '673':
        print ps, "good for", pps
    else:
      return ps
  return "[result]"

@benchmark
def brute_force():
  primes = [673,109,7,3]
  for p in prime(673,1e6):
    ps = str(p)
    for pp in primes:
      pps = str(pp)
      if not is_prime(int(pps+ps)):
        break
      if not is_prime(int(ps+pps)):
        break
      if pps != '673':
        print p, "good for", pps
    else:
      return p
  return "[result]"

if __name__ == "__main__":
  solve()