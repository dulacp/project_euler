#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 083
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
      if i == 0 and j == 0:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i,j+1)) # right
      elif i == 0 and j == m.shape[1]-1:
        g.AddEdge(node(i,j), node(i+1,j)) # down
      elif i == m.shape[0]-1 and j == m.shape[1]-1:
        g.AddEdge(node(i,j), node(i-1,j)) # up
      elif i == m.shape[0]-1 and j == 0:
        g.AddEdge(node(i,j), node(i,j+1)) # right
      elif i == 0:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i,j+1)) # right
      elif j == 0:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j+1)) # right
      elif j == m.shape[1]-1:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j-1)) # left
      elif i == m.shape[0]-1:
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j+1)) # right
      else:
        g.AddEdge(node(i,j), node(i+1,j)) # down
        g.AddEdge(node(i,j), node(i-1,j)) # up
        g.AddEdge(node(i,j), node(i,j+1)) # right
        g.AddEdge(node(i,j), node(i,j-1)) # left
  return g

@benchmark
def solve():
  g = UndirectedGraphFromMatrix(m)
  leading_node, terminating_node = node(0,0), node(m.shape[0]-1, m.shape[1]-1)
  print "graph loaded"

  minpath = DjikstraMinPath(g,leading_node,terminating_node, weight_func=w)
  return sum(w(n) for n in minpath)

if __name__ == "__main__":
  solve()