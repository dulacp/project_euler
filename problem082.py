#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 082
#

from decorators import benchmark
from decorators import memoized
from graph import *
import numpy as np

#m = np.matrix('131 673 ; 201 96')
#m = np.matrix('131 673 234 103 18 ; 201 96 342 965 150 ; 630 803 746 422 111 ; 537 699 497 121 956 ; 805 732 524 37 331')
#m = np.matrix( open('problem081_smallmatrix.txt').read().replace('\n',';') )
m = np.matrix( open('problem081_matrix.txt').read().replace('\n',';') )
print "matrix %s loaded" % str(m.shape)

w = lambda n: n[-1]
node = lambda i,j: (i,j,m[i,j])

def UndirectedGraphFromMatrix(m):
  g = UndirectWeigtedGraph()
  for i in range(m.shape[0]):
    for j in range(m.shape[1]):
      if j == m.shape[1]-1:
        g.AddNode((i,j,m[i,j]))
      elif i == 0:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i,j+1)) # right
      elif i == m.shape[0]-1:
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j+1)) # right
      else:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j+1)) # right
  return g

@benchmark
def solve():
  """
  The idea is to add a leading node and a terminating node
  with a weight of 0
  like this graph for a M(3,3) matrix

                  - (0,0) - (0,1) - (0,2) -
                /                           \
  leading node ---- (1,0) - (1,1) - (1,2) ----- terminating node
                \                           /
                  - (2,0) - (2,1) - (2,2) - 

  """
  g = UndirectedGraphFromMatrix(m)
  leading_node, terminating_node = (-1,-1,0), (m.shape[0], m.shape[1], 0)
  for i in range(m.shape[0]): g.AddEdge(leading_node, node(i,0))
  for i in range(m.shape[1]): g.AddEdge(node(i,m.shape[1]-1), terminating_node)
  print "graph loaded"

  minpath = DjikstraMinPath(g,leading_node,terminating_node, weight_func=w)
  return sum(w(n) for n in minpath)

# time: about 6400s to find the answer (based on 1s for Djikstra algo)
@benchmark
def slow():
  g = UndirectedGraphFromMatrix(m)
  print "graph loaded"

  minpathlength = float('inf')
  for i in range(m.shape[0]):
    for j in range(m.shape[1]):
      from_node, target_node = node(i,0), node(j,m.shape[1]-1)
      minpath = DjikstraMinPath(g,from_node,target_node, weight_func=w)
      minpathlength = min(minpathlength, sum(w(n) for n in minpath))
      #print from_node, target_node, minpathlength
  #print minpath
  return minpathlength

if __name__ == "__main__":
  solve()
  #slow()