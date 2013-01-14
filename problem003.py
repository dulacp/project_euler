#!/usr/bin/env python
#
# The Euler Project: problem 3

import math
import time
from prime import *

t_start = time.time()

limit = 600851475143
start = int(math.sqrt(limit))
start = start if start%2==1 else start+1

for i in xrange(start, 0, -2):
  if is_prime(i) and limit % i == 0:
    break

t_end = time.time()

print i
print "temps d'execution: %f s" % (t_end - t_start)