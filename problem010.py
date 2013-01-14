#!/usr/bin/env python
#
# The Euler Project: problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from decorators import benchmark
from prime import *

@benchmark
def solve():
  print sum([p for p in prime(limit=2e6)])

if __name__ == '__main__':
  solve()