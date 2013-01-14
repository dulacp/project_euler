"""
Helpers for permutations
"""

def couple(digits, length, optimized=True):
  sdigits = map(str, digits)
  if length == 1:
    for c in sdigits:
      yield [c]
  else:
    for i in range(len(sdigits)):
      for c in couple(sdigits[(i if optimized else 0):], length-1, optimized=optimized):
        yield [sdigits[i]] + c

def permut(digits=range(3)):
  sdigits = map(str, digits)
  d = sdigits[0]
  if len(sdigits) == 1:
    yield [d]
  else:
    for p in permut(sdigits[1:]):
      for i in range(len(p)+1):
        pp = list(p)
        pp.insert(i,d)
        yield ''.join(pp)

def circular_permut(digits=range(3)):
  sdigits = map(lambda d: str(d), digits)
  for i in range(len(sdigits)):
    yield ''.join(sdigits[i:] + sdigits[:i])