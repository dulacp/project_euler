#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 31
#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
# How many different ways can £2 be made using any number of coins?

import time

class Node:
  def __init__(self, value=0, parent=None):
    self.value = value
    self.parent = parent

  def __add__(self, other):
    return self.value + other.value

  def __str__(self):
    return str(self.parent) + " -> %d" % self.value

  def sum(self):
    if self.parent is None:
      return self.value
    return self.parent.sum() + self.value

# test
i1 = Node(3)
i2 = Node(4,i1)
i3 = Node(8,i2)
print i3, i3.parent, i3.sum()

coins = [100, 50, 20, 10, 5, 2, 1] # in pounds
amount = 200 # amount to make with coins combination

def graph(coins, amount, parent_node=None, recursion_level=0):
  nodes = []
  for i,c in enumerate(coins[:]):
    if c > amount: 
      continue
    elif c == amount: 
      nodes.append(Node(c, parent_node))
    else: 
      #print " "*recursion_level, parent_node
      parent = Node(c, parent_node)
      nodes.extend(graph(coins[i:], amount-c, parent, int(recursion_level)+1))
  return nodes

#for n in graph(coins, 10):
#  print n.sum(), n
t_start = time.time()
print "comb =", 1+len(graph(coins, 200)) # +1 because there is the 200 coin combi
t_end = time.time()
print "time: %f s" % (t_end - t_start)