#!/usr/bin/env python
#
# The Euler Project: problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is 
# one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
# are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Super smart but not me :/ (about 12ms)
import math

nums=range(10)
order=999999
newnum=[]

for i in range(9,-1,-1):
    digit=order/math.factorial(i)
    newnum.append(nums.pop(digit))

    order-=digit*math.factorial(i)

print ''.join(map(str, newnum))

# Me :) (about 10 sec)
def permut(digits=range(3)):
  sdigits = [str(d) for d in digits]
  d = sdigits[0]
  if len(sdigits) == 1:
    yield [d]
  else:
    for p in permut(sdigits[1:]):
      for i in range(len(p)+1):
        pp = list(p)
        pp.insert(i,d)
        yield ''.join(pp)

permuts = [p for p in permut(range(10))]
permuts.sort()
print permuts[int(1e6)-1]