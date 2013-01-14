#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 084
#

from decorators import benchmark
from collections import defaultdict
from copy import copy, deepcopy
import numpy as np

DICE_FACES = 6

squares = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',\
  'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2',  'D3', \
  'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2',  'F3', \
  'G2J','G1', 'G2', 'CC3','G3', 'R4', 'CH3', 'H1','T2', 'H2']

@benchmark
def solve():
  def dices_probas(dice_faces=6, depth_limit=3):
    def _proba(depth=1):
      d = defaultdict(dict)
      for i in range(1,dice_faces+1):
        for j in range(1,dice_faces+1):
          if i == j and depth <= depth_limit:
            d[(i,j)] = _proba(depth+1)
          else:
            d[(i,j)] = (1./dice_faces)**(2*depth)
      return d
    return _proba(1)

  probas = dices_probas(dice_faces=DICE_FACES)
  def recursive_sum(p):
    if isinstance(p, dict):
      return sum(recursive_sum(p[k]) for k in p)
    return p

  # test recursive_sum
  epsilon = 1e10
  assert abs(recursive_sum(probas[(1,1)]) - 1./36) < epsilon
  assert abs(recursive_sum(probas[(1,1)][(1,1)]) - (1./36)**2) < epsilon
  print "CHECK SUM : {0}%".format(round(recursive_sum(probas)*100),2)
  
  square_probas = np.zeros(len(squares))
  def recurisve_play(dice_throws, initial_square=0, depth=1):
    for c in dice_throws:

      sq_index = (initial_square+sum(c)) % len(squares)
      sq = squares[sq_index]
      p = recursive_sum(dice_throws[c])

      if depth > 3 and c[0]==c[1]: # directly to jail because of the third double
        square_probas[squares.index('JAIL')] += p
        continue
      if sq == 'G2J': # directly to jail
        square_probas[squares.index('JAIL')] += p
        continue

      def recursive_ratio(p, r):
        if isinstance(p, dict):
          return {k: recursive_ratio(p[k], r) for k in p}
        return p*r

      def next_station(sqi):
        if 35 <= sqi or sqi < 5: return 5
        elif 5 <= sqi < 15: return 15
        elif 15 <= sqi < 25: return 25
        elif 25 <= sqi < 35: return 35

      if sq[:2] == 'CH': # chance (pick a card)
        # Chance (10/16 cards):
        # Advance to GO
        # Go to JAIL
        # Go to C1
        # Go to E3
        # Go to H2
        # Go to R1
        # Go to next R (railway company)
        # Go to next R
        # Go to next U (utility company)
        # Go back 3 squares.
        #
        if c[0] == c[1]: # double (tricky)
          square_probas[squares.index('JAIL')] += p*1./16
          
          # tirer une carte et avoir un mouvement revient finalement à un lancé de dé du nombre de cases équivalentes
          potential_squares = map(lambda a: squares.index(a), ['GO','C1','E3','H2'])
          potential_squares += [next_station(sq_index)]
          potential_squares += [12 if sq_index < 12 or sq_index >= 28 else 28]
          potential_squares += [sq_index-3]
          new_throws = {(0,(k-sq_index)%len(squares)):recursive_ratio(dice_throws[c], 1./16) for k in potential_squares}

          # next station (two cards of this kind)
          k_next_station = (0, (next_station(sq_index)-sq_index)%len(squares))
          new_throws[k_next_station] = recursive_ratio(new_throws[k_next_station], 2)

          # R1 station
          k_first_station = (0, (squares.index('R1')-sq_index)%len(squares))
          if k_first_station in new_throws: new_throws[k_first_station] = recursive_ratio(new_throws[k_first_station], 3./2)
          else: new_throws[k_first_station] = recursive_ratio(dice_throws[c], 1./16)

          recurisve_play(new_throws, sq_index, depth)
          p *= 6./16

        else:
          square_probas[squares.index('GO')] += p*1./16
          square_probas[squares.index('JAIL')] += p*1./16
          square_probas[squares.index('C1')] += p*1./16
          square_probas[squares.index('E3')] += p*1./16
          square_probas[squares.index('H2')] += p*1./16
          square_probas[squares.index('R1')] += p*1./16
          square_probas[next_station(sq_index)] += 2*p*1./16 # two cards of this kind
          square_probas[12 if sq_index < 12 or sq_index > 28 else 28] += p*1./16
          square_probas[sq_index-3] += p*1./16
          p *= 6./16

      if sq[:2] == 'CC': # community chest (pick a card)
        # Community Chest (2/16 cards):
        # Advance to GO
        # Go to JAIL
        #
        if c[0] == c[1]: # double (tricky)
          square_probas[squares.index('JAIL')] += p*1./16
          # tirer une carte et avoir un mouvement revient finalement à un lancé de dé du nombre de cases équivalentes
          potential_squares = [squares.index('GO')]
          new_throws = {(0,(k-sq_index)%len(squares)):recursive_ratio(dice_throws[c], 1./16) for k in potential_squares}
          recurisve_play(new_throws, sq_index, depth)
          p *= 14./16
        else:
          square_probas[squares.index('GO')] += p*1./16
          square_probas[squares.index('JAIL')] += p*1./16 # BOF... à améliorer
          p *= 14./16

      p0 = recursive_sum(dice_throws[c])
      r = p/p0
      
      if r != 1:
        #assert abs(recursive_sum(dice_throws[c])*r - recursive_sum(recursive_ratio(dice_throws[c], r))) < epsilon
        dice_throws[c] = recursive_ratio(dice_throws[c], r)

      if c[0]==c[1]: # double
        recurisve_play(dice_throws[c], sq_index, depth+1)
      else: # normal throw
        square_probas[sq_index] += p

  for i in range(len(squares)):
    print "play with initial square {0}".format(squares[i])
    probas = dices_probas(dice_faces=DICE_FACES)
    recurisve_play(probas, i, 1)

  # divide by the number of squares
  square_probas /= len(squares)
  print square_probas
  print "TOTAL : {0}%".format(round(sum(square_probas[k]*100 for k in range(len(squares))), 6))

  # sort the most popular squares
  square_probas_sorted = [(squares[k], square_probas[k]) for k in range(len(squares))]
  square_probas_sorted.sort(key=lambda a: a[1], reverse=True)
  for k,v in square_probas_sorted:
    print "{0:6} {1}%".format(k, round(v*100, 2))

  return ''.join(map(lambda a: str(a) if len(str(a)) == 2 else '0'+str(a), \
    [squares.index(c[0]) for c in square_probas_sorted[:3]]))

if __name__ == "__main__":
  solve()