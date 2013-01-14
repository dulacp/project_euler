#!/usr/bin/env python
#
# The Euler Project: problem 18
#
# By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23.
#
#       3
#      7 4
#     2 4 6
#    8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#                            75
#                           95 64
#                          17 47 82
#                         18 35 87 10
#                        20 04 82 47 65
#                       19 01 23 75 03 34
#                      88 02 77 73 07 63 67
#                     99 65 04 28 06 16 70 92
#                    41 41 26 56 83 40 80 70 33
#                   41 48 72 33 47 32 37 16 94 29
#                  53 71 44 65 25 43 91 52 97 51 14
#                 70 11 33 28 77 73 17 78 39 68 17 57
#                91 71 52 38 17 14 91 43 58 50 27 29 48
#               63 66 04 68 89 53 67 30 73 16 69 87 40 31
#              04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by 
# trying every route. However, Problem 67, is the same challenge with a triangle 
# containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

import numpy as np

test = "3\n\
7 4\n\
2 4 6\n\
8 5 9 3"

s = "75\n\
95 64\n\
17 47 82\n\
18 35 87 10\n\
20 04 82 47 65\n\
19 01 23 75 03 34\n\
88 02 77 73 07 63 67\n\
99 65 04 28 06 16 70 92\n\
41 41 26 56 83 40 80 70 33\n\
41 48 72 33 47 32 37 16 94 29\n\
53 71 44 65 25 43 91 52 97 51 14\n\
70 11 33 28 77 73 17 78 39 68 17 57\n\
91 71 52 38 17 14 91 43 58 50 27 29 48\n\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\n\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

data = s
#data = test

nlines = len(data.split('\n'))
A = np.zeros((nlines, nlines), dtype=int)

# fill the matrix
for i,l in enumerate(data.split('\n')):
  for j,n in enumerate(l.split(' ')):
    A[i][j] = int(n)
print A
print

# compute the optimal path (with the larger sum)
triangle = A
j = 0
weights = [A[0,0]]
for i in range(1,A.shape[0]):
  # guess if we choose the inf triangle or the sup triangle to continue
  inf = np.tril(triangle, k=-(i-j))
  sup = np.array(triangle)
  sup[:,0:j+1] = 0

  print triangle
  print inf
  print sup
  print inf.sum(), sup.sum()
  print weights
  if inf.sum() > sup.sum():
    triangle = inf
    weights.append(triangle[i,j])
    print "inf choosed (%d,%d) = %d" % (i,j, triangle[i,j])
  else:
    triangle = sup
    j += 1
    weights.append(triangle[i,j])
    print "sup choosed (%d,%d) = %d" % (i,j, triangle[i,j])

  #raw_input()

print "weights", weights
print "len", len(weights)
print "total", sum(weights)

def brute_force():
  print "\nBrut Force"
  paths = [ [(0,0, A[0,0])] ]
  for i in range(1,A.shape[0]):
    new_paths = []
    for p in paths:
      last = p[-1]
      pp = p[:]
      p.append( (i,last[1], A[i,last[1]]) )
      pp.append( (i,last[1]+1, A[i,(last[1]+1)]) )
      new_paths.append(pp)
    paths.extend(new_paths)
  lengths = [(sum(a[2] for a in p),p) for p in paths]
  print max(lengths, key=lambda a: a[0])
  #print [len(p) for p in paths]

brute_force()
