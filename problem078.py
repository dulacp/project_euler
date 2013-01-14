#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 078
#

from decorators import benchmark
from decorators import memoized
from prime import gcd
import math

N = 10**6

@benchmark
def solve():
  plist,n = [1], 1

  @memoized
  def pentagonal_number(i):
    return i*(3*i - 1)/2

  while plist[-1]:
    p,i = 0,1
    while pentagonal_number(i) <= n:
      pt = pentagonal_number(i)
      if pt <= n:
        p += ((-1)**(i+1)) * (plist[n - pt])
      pt = pentagonal_number(-i)
      if pt <= n:
        p += ((-1)**(i+1)) * (plist[n - pt])
      i += 1
    plist.append(p%N)
    n += 1
  return n-1, plist

# answer 2858724 and it took 1388.778634 s
# NB: 2858724 = 183*5**6 - 651
@benchmark
def fast_but_wrong():
  """
  http://mathworld.wolfram.com/PartitionFunctionPCongruences.html

  and divisble by 10**6 = 2**6 * 5**6  (prime factorisation)

  Watson (1938) then proved the general congruence
  P(n) congru 0 (mod 5^a) if 24*n congru 1 (mod 5^a)

  cad   
  24*n = b*5**6 + 1 = b*(15625) + 1
  so we can deduce n

  n = k*5**6 - 651 for k >= 1

  and we want P(n) = b'*1 000 000
  so P(k*5**6 - 651) = b'*1 000 000
  """
  plist = [1,1,2,3,5]
  def euler_p(n):
    if n >= len(plist):
      pn = 0
      for k in range(1,n+1):
        k1 = int(n - 1./2*k*(3*k-1))
        k2 = int(n - 1./2*k*(3*k+1))
        if k1 >= 0:
          pn += ((-1)**(k+1))*(euler_p(k1))
        if k2 >= 0:
          pn += ((-1)**(k+1))*(euler_p(k2))
      plist.append(pn)
    return plist[n]

  from sympy.ntheory import npartitions
  k = 1
  while True:
    n = k*5**6 - 651
    #n = k

    # # p(7*k + 5) congru 0 (mod 7)
    # if (n-5)%7==0:
    #   print "p(%d) divisible par 7" % n
    # # p(11*k + 6) congru 0 (mod 11)
    # elif (n-6)%11==0:
    #   print "p(%d) divisible par 11" % n
    # # p(11**3 * 13 * k + 237) congru 0 (mod 13)
    # elif (n-237)%(13*11**3)==0:
    #   print "p(%d) divisible par 13" % n
    # else:
    p = npartitions(n)

    # show that there is often a error of 1 in the npartitions result
    # if p != euler_p(n):
    #   print "NANNNN", p, euler_p(n)
    #   raw_input()

    if (p-1)%N==0 or p%N==0 or (p+1)%N==0:
      print "Potential", n, p
      print " compute euler value"
      print "", euler_p(n)
      raw_input("continue ?")
    else:
      print "OUT", n, str(p)[-10:]
    k += 1
  return n,p

@benchmark
def still_slow():
  """Euler generating function"""
  plist = [1,1,2,3,5]
  def euler_p(n):
    if n >= len(plist):
      pn = 0
      for k in range(1,n+1):
        k1 = int(n - 1./2*k*(3*k-1))
        k2 = int(n - 1./2*k*(3*k+1))
        if k1 >= 0:
          pn += ((-1)**(k+1))*(euler_p(k1))
        if k2 >= 0:
          pn += ((-1)**(k+1))*(euler_p(k2))
      plist.append(pn)
    return plist[n]

  n = 2
  while True:
    p = euler_p(n)
    if n > 1 and p%N == 0:
      break
    n += 1
  return n, p

@benchmark
def slow():
  """
  http://en.wikipedia.org/wiki/Partition_(number_theory)
  """
  from prime import divisors_sigma
  p = [1]
  n = 1
  while True:
    p.append( 1./n*sum(divisors_sigma(n-k)*p[k] for k in range(0,n)) )
    #print n, p[-1]
    if n > 1 and p[-1]%N == 0:
      break
    n += 1
  return n, int(p[-1])

if __name__ == "__main__":
  solve()
  #fast_but_wrong()
  still_slow()
  slow()