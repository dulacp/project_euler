#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 145
#
# Some positive integers n have the property that the sum [ n + reverse(n) ] 
# consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
# We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. 
# Leading zeroes are not allowed in either n or reverse(n).
#
# There are 120 reversible numbers below one-thousand.
#
# How many reversible numbers are there below one-billion (109)?

from decorators import benchmark

N = 1e4

@benchmark
def solve():
    import math
    wrong = '02468'
    def is_reversible(a):
        if a % 10 == 0: return False
        a = str(a)
        a = str(int(a) + int(a[::-1]))
        for w in wrong:
            if w in a:
                return False
        return True

    def is_r(a):
        if a%10 == 0:
            return False
        a = str(a)
        r = 0
        for j in range(len(a)):
            s = int(a[j]) + int(a[-j-1]) + r
            r = s/10
            if s%2 == 0:
                return False
        return True

    i,c = 12,0
    while i < N:
        if is_r(i):
            c += 1
        i += 1
        
    return c

@benchmark
def semi_solve():
    import math
    wrong = ['0', '2', '4', '6', '8']
    def is_reversible(a):
        if a%10 == 0:
            return False
        a = str(a)
        r = 0
        #print "--", a
        #for j in range(int(math.ceil(len(a)/2.))):
        for j in range(len(a)):
            s = int(a[j]) + int(a[-j-1]) + r
            #print s
            r = s/10
            if s%2 == 0:
                return False
        return True

    c = 0
    for i in xrange(int(N)):
        if is_reversible(i):
            c += 1
    return c

@benchmark
def brute_force():
    wrong = ['0', '2', '4', '6', '8']
    def is_reversible(a):
        if a % 10 == 0: return False
        a = str(a)
        a = str(int(a) + int(a[::-1]))
        for aa in a:
            if aa in wrong:
                return False
        return True

    c = 0
    for i in xrange(int(N)):
        if is_reversible(i):
            c += 1
    return c

if __name__ == "__main__":
    solve()
    semi_solve()
    brute_force()