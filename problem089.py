#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 089
#

from decorators import benchmark

@benchmark
def solve():
  roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  authorized_subtrat_couples = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

  substrat_couple_map = {k:roman_map[k[-1]]-roman_map[k[0]] for k in authorized_subtrat_couples}

  reverse_map = {v:k for k,v in roman_map.items()}
  reverse_map.update({v:k for k,v in substrat_couple_map.items()})

  reverse_sorted_keys = reverse_map.keys()
  reverse_sorted_keys.sort(reverse=True)

  #print reverse_map
  #print reverse_sorted_keys
  #raw_input()

  def parse(s):
    d = 0
    for i in range(len(s)-1):
      if roman_map[s[i]] < roman_map[s[i+1]]:
        d -= roman_map[s[i]]
      else:
        d += roman_map[s[i]]
    return d + roman_map[s[-1]]

  def minimal(d):
    """Minimal Roman representation"""
    s = []
    while d > 0:
      i = 0
      while i+1 < len(reverse_sorted_keys) and reverse_sorted_keys[i] > d:
        i += 1
      k = reverse_sorted_keys[i]
      s.append(reverse_map[k])
      d -= k
    return s

  count = 0
  with open('problem089_roman.txt') as f:
    for l in f:
      l = l.strip()
      m = ''.join(minimal(parse(l)))
      print "{0:20} {1:<8} {2:<20} {3}".format(l, parse(l), ''.join(minimal(parse(l))), len(l) - len(m))
      count += len(l) - len(m)

  return count

if __name__ == "__main__":
  solve()