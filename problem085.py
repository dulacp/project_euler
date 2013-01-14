#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 085
#

from decorators import benchmark

N = 2*10**6

@benchmark
def solve():

  def better_rectangles_count(w,h):
    return w*(w+1)*h*(h+1)/4

  def rectangles_count(width, length):
    s = 0
    for i in range(1,width+1):
      for j in range(1,length+1):
        s += (width-i+1)*(length-j+1)
    return s

  l,L=3,2
  while rectangles_count(l,L) < N:
    l += 1
  starting_couple = (l,L)
  print "first couple %s -> %d" % (starting_couple,better_rectangles_count(l,L))

  next_couple = lambda couple: (couple[0], couple[1]+1)
  next_couple_direction = lambda couple, direction: (couple[0]+direction, couple[1])
  direction_condition = lambda couple, direction: direction*better_rectangles_count(*couple) < direction*N

  current_couple = starting_couple
  current_direction = 1

  m = (0,0,0)
  while current_couple == starting_couple or current_couple[0] >= current_couple[1]:
    current_couple = next_couple(current_couple)
    while direction_condition(current_couple, current_direction):
      current_couple = next_couple_direction(current_couple, current_direction) # FAILLE petite mais faille quand meme ^^
    #print "%s -> %d" % (current_couple, rectangles_count(current_couple[0], current_couple[1]))
    m = min(m, (better_rectangles_count(*current_couple), current_couple[0], current_couple[1]), \
      key=lambda a: abs(N-a[0]))
    current_direction *= -1

  return m[1]*m[2]

if __name__ == "__main__":
  solve()