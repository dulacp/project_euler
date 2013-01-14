#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 081
#

from decorators import benchmark
from decorators import memoized
import numpy as np

@benchmark
def solve():
  #m = np.matrix('131 673 ; 201 96')
  #m = np.matrix('131 673 234 103 18 ; 201 96 342 965 150 ; 630 803 746 422 111 ; 537 699 497 121 956 ; 805 732 524 37 331')
  m = np.matrix( open('problem081_matrix.txt').read().replace('\n',';') )
  print "matrix %s loaded" % str(m.shape)

  @memoized
  def min_path(root_line, root_column):
    if root_line == m.shape[0]-1 and root_column == m.shape[1]-1:
      return m[-1,-1]
    elif root_line == m.shape[0]-1:
      r = l = min_path(root_line,root_column+1)
    elif root_column == m.shape[1]-1:
      r = l = min_path(root_line+1,root_column)
    else:
      l = min_path(root_line+1,root_column)
      r = min_path(root_line,root_column+1)
    return m[root_line,root_column] + min(l,r)

  return min_path(0,0)

if __name__ == "__main__":
  solve()