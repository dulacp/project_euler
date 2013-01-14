#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 076
#

from decorators import benchmark

N = 100
integers = range(1,N)

@benchmark
def solve():
  """
  http://en.wikipedia.org/wiki/Partition_(number_theory)
  """
  from prime import divisors_sigma
  p = [1]
  for n in range(1,N+1):
    p.append( 1./n*sum(divisors_sigma(n-k)*p[k] for k in range(0,n)) )
  return int(p[-1]-1)

@benchmark
def still_slow():
  def graph(coins, amount, partial_sum=0):
    count = 0
    for i,c in enumerate(coins):
      if c > amount:
        continue
      elif c == amount: 
        count += 1
      else: 
        partial_sum += c
        count += graph(coins[i:], amount-c, partial_sum)
    return count
  return graph(integers, N)

@benchmark
def slow():
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

  g = graph(integers, N)
  # for n in g: print n
  return len(g)

@benchmark
def brute_force():
  count = 0
  from permut import couple
  for n in range(N,1,-1):
    for c in couple(integers,n):
      if reduce(lambda x,y: x+int(y),c, 0) == N:
        #print c
        count += 1
  return count

if __name__ == "__main__":
  solve()
  still_slow()
  slow()
  brute_force()