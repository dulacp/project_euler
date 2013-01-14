#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 47
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 x 7
# 15 = 3 x 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² x 7 x 23
# 645 = 3 x 5 x 43
# 646 = 2 x 17 x 19.
#
# Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

import time
from prime import *

P = Prime([2,3,5])
for p in P.gen(index_limit=100):
  pass
print "primes array loaded"

def prime_factors(x, compute_pows=True):
  f = []
  for p in P.gen():
    if p > x:
      break
    if x%p == 0:
      i = 1
      while x%(p**(i+1))==0:
        i += 1
      if compute_pows: f.append(p**i)
      else: f.extend(i*[p])
      x /= p
    if x == 1:
      break
  return f


# smarter solution
# def larger_factor_pow(a,x):
#   i = 1
#   while a%(x**(i+1))==0:
#     i += 1
#   return i

# t = time.time()
# couple = i,j,k,l = 644,645,646,647
# i_f,j_f,k_f,l_f = [set(prime_factors(n)) for n in couple]
# for a in xrange(i+1, 10**8):
#   i,j,k,l = a,a+1,a+2,a+3

#   # speed up
#   if a%2==0:
#     aa = a+2
#     i,ii = larger_factor_pow(a,2), larger_factor_pow(aa,2)
#     if i == ii:
#       continue
#   else:
#     aa = a+3
#     i,ii = larger_factor_pow(a+1,2), larger_factor_pow(aa,2)
#     if i == ii:
#       continue
#   if a%3==0:
#     aa = a+3
#     i,ii = larger_factor_pow(a,2), larger_factor_pow(aa,2)
#     if i == ii:
#       continue

#   # full checking
#   i_f, j_f, k_f, l_f = [set(prime_factors(n)) for n in (i,j,k,l)]
#   if len(i_f)+len(j_f)+len(k_f)+len(l_f) != 16:
#     continue
#   print i,j,k,l
#   print i_f, j_f, k_f, l_f
#   if not i_f.intersection(j_f).intersection(k_f).intersection(l_f):
#     print "found!"
#     break

# print i,j,k
# print "time: %f s" % (time.time() - t)


# brute force! (251 secondes to find :/)
t = time.time()
couple = i,j,k,l = 644,645,646,647
i_f,j_f,k_f,l_f = [set(prime_factors(n)) for n in couple]
for a in xrange(k+1, 10**8):
  i,j,k,l = j,k,l,a
  i_f, j_f, k_f, l_f = j_f, k_f, l_f, set(prime_factors(a))
  if len(i_f)+len(j_f)+len(k_f)+len(l_f) != 16:
    continue
  print i,j,k,l
  print i_f, j_f, k_f, l_f
  if not i_f.intersection(j_f).intersection(k_f).intersection(l_f):
    print "found!"
    break

print i,j,k
print "time: %f s" % (time.time() - t)