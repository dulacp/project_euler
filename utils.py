# -*- coding: utf-8 -*-

"""
Utils
"""

import math

is_square = lambda x: x == math.pow(round(math.pow(x,1./2)),2)

def frange(limit1, limit2=None, increment=1.):
  """
  Range function that accepts floats (and integers).

  Usage:
  frange(-2, 2, 0.1)
  frange(10)
  frange(10, increment = 0.5)

  The returned value is an iterator.  Use list(frange) for a list.
  """
  if limit2 is None:
    limit2, limit1 = limit1, 0.
  else:
    limit1 = float(limit1)
  count = int(math.ceil(limit2 - limit1)/increment)
  return (limit1 + n*increment for n in range(count))