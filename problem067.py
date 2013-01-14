#!/usr/bin/env python
#
# The Euler Project: problem 67
#
# same as probleme 18 but with a bigger binary tree

# Shortest solution from online thread
#
# tab = [[int(n) for n in s.split()] for s in open('N67.txt').readlines()]
# nb = 0
# index = 0
# for i in range(len(tab)-1,0,-1):
#   for j in range(0,len(tab[i-1])):
#     tab[i-1][j] += max(tab[i][j],tab[i][j+1])
# print(tab[0][0])

from decorators import benchmark
from decorators import memoized

class Node:
  def __init__(self, value=0, left=None, right=None, parent_left=None, parent_right=None):
    self.value = value
    self.left = left
    self.right = right
    self.parent_left = parent_left
    self.parent_right = parent_right

  def __str__(self):
    return str(self.parent) + " -> %d" % self.value

def load_tree(filename):
  root = None
  parents = []
  for l in open(filename):
    if root is None:
      root = Node(int(l))
      parents = [root]
      continue
    newparents = []
    for i,v in enumerate(l.split(' ')):
      n = Node(int(v))
      if i < len(parents):
        n.parent_right = parents[i]
        parents[i].left = n
      if i > 0:
        n.parent_left = parents[i-1]
        parents[i-1].right = n
      newparents.append(n)
    parents = newparents
  return root

@benchmark
def solve():
  root = load_tree('problem067_triangle.txt')

  @memoized
  def max_path(root_node, recursion_index=0):
    if root_node is None:
      return 0
    l = max_path(root_node.left, recursion_index+1)
    r = max_path(root_node.right, recursion_index+1)
    return root_node.value + max(l,r)

  return max_path(root)

if __name__ == "__main__":
  solve()