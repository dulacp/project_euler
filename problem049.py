#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 49
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
# by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) 
# each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

import time
from collections import defaultdict

from prime import *
from permut import *

t = time.time()

for c in couple(range(10), length=4):
  primes = set([int(p) for p in permut(c) if len(str(int(p))) == 4 and is_prime(int(p))])
  if len(primes) <= 2:
    continue
  
  l = sorted(list(primes))
  dist = list( ((p1,p2),p2-p1) for p1 in l for p2 in l if p2>p1 )
  dist.sort(key=lambda x:x[0][0])
  seqs = defaultdict(list)
  for p1p2,d in dist:
    if not seqs[d] or any(p1p2[0]==pp1pp2[1] for pp1pp2 in seqs[d]):
      seqs[d].append(p1p2)
  for k,v in seqs.items():
    if len(v) <= 1:
      del seqs[k]
    v.sort(key=lambda x: x[0])
  if seqs:
    for v in seqs.values():
      print ''.join(map(lambda x: str(x), [v[0][0]] + [v[i][1] for i in range(len(v))]))

print "time: %f s" % (time.time() - t)