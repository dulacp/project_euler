#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 000
#

from decorators import benchmark
from collections import defaultdict
from permut import *
from utils import *


@benchmark
def solve():
  # find the anagrams
  anagrams = defaultdict(list)
  with open('problem098_words.txt') as f:
    words = map(lambda s: s.strip('"'), f.read().split(','))
    for w in words: 
      k = ''.join(sorted(list(w)))
      if w[::-1] not in anagrams[k]: # because palindromic words are not anagrams
        anagrams[k].append(w)

  # filter the non-anagrams (and find the largest one)
  largest_anagram_size = 0
  for k in anagrams.keys():
    if len(anagrams[k]) == 1: 
      del anagrams[k]
    else:
      largest_anagram_size = max(largest_anagram_size, len(k))
  print "largest anagram size:", largest_anagram_size

  # load the squares
  lookup_squares = []
  i,s = 1,""
  while len(s) <= largest_anagram_size:
    s = str(i**2)
    lookup_squares.append(s)
    i += 1
  print "squares loaded"
  #print lookup_squares

  # find squares anagrams
  anagram_squares = defaultdict(list)
  for s in lookup_squares:
    k = ''.join(sorted(list(s)))
    anagram_squares[k].append(s)

  # filter the non-anagrams squares (and find the largest one)
  for k in anagram_squares.keys():
    if len(anagram_squares[k]) == 1: 
      del anagram_squares[k]
  #print anagram_squares

  # sort anagram_squares by size
  anagram_squares_sized_organized = defaultdict(list)
  for k in anagram_squares:
    anagram_squares_sized_organized[len(k)].append(anagram_squares[k])
  #print anagram_squares_sized_organized

  def find_squares(anagram_pair):
    squares_list = []
    first_anagram, second_anagram = anagram_pair
    for clist in anagram_squares_sized_organized[len(first_anagram)]:
      for c in clist:
        squares = [c] # reset

        # build the digit map
        map_letter_to_int = {}
        for i,l in enumerate(first_anagram):
          if l in map_letter_to_int and map_letter_to_int[l] != c[i]:
            # continue to the next 'c' (due to the for:else: clause)
            break
          elif l not in map_letter_to_int and c[i] in map_letter_to_int.values():
            # continue to the next 'c' (due to the for:else: clause)
            break
          else:
            map_letter_to_int[l] = c[i]
        else: # else of the for loop (to execute this only if break was not called)
          #print first_anagram, map_letter_to_int
          #raw_input()
          second_anagram_to_int = ''.join([map_letter_to_int[l] for l in second_anagram])
          if second_anagram_to_int[0] == '0':
            continue
          if second_anagram_to_int in clist:
            squares.append(second_anagram_to_int)
            squares_list.append(squares)
    return squares_list

  # test 
  test_pair = ('CARE', 'RACE')
  print "TEST", test_pair, find_squares(test_pair)
  print "TEST", test_pair, anagram_squares_sized_organized[len(test_pair[0])]

  # run the function on each anagram pair
  S = 0
  for k in anagrams:
    for i in range(len(anagrams[k])):
      for j in range(i+1, len(anagrams[k])):
        pair = (anagrams[k][i], anagrams[k][j])
        squares = find_squares(pair)
        print pair, squares
        if squares:
          S = max(S, max(max(map(int,s) for s in squares)))

  return S

if __name__ == "__main__":
  solve()