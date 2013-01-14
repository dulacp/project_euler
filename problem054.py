#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 54
#
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; 
# for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, 
# for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); 
# if the highest cards tie then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand    Player 1          Player 2          Winner
# 1       5H 5C 6S 7S KD    2C 3S 8S 8D TD    Player 2
#         Pair of Fives     Pair of Eights
#   
# 2       5D 8C 9S JS AC    2C 5C 7D 8S QH    Player 1
#         Highest card Ace  Highest card Queen
#   
# 3       2D 9C AS AH AC    3D 6D 7D TD QD    Player 2
#         Three Aces        Flush with Diamonds
#   
# 4       4D 6S 9H QH QC    3D 6D 7H QD QS    Player 1
#         Pair of Queens    Pair of Queens
#         Highest card Nine Highest card Seven
#   
# 5       2H 2D 4C 4D 4S    3C 3D 3S 9S 9D    Player 1
#         Full House        Full House
#         With Three Fours  with Three Threes
# 
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the first five 
# are Player 1's cards and the last five are Player 2's cards. You can assume that all hands 
# are valid (no invalid characters or repeated cards), each player's hand is in no specific order, 
# and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

import time
t = time.time()

def smart():
  """by Kutta"""
  from collections import Counter
  pairs = (line.split() for line in open('problem054_poker.txt'))
  values = {r:i for i,r in enumerate('23456789TJQKA')}

  def hand_comp(hand):
    comp = zip(*sorted(((v,values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True))
    print comp
    if len(comp[0]) == 5:
      unicolor = len({x[1] for x in hand}) == 1
      straight = comp[1] == tuple(range(comp[1][0], comp[1][-1]-1, -1))
      comp[0] = ((1, (3,2,1)), ((3,2,0), 5))[straight][unicolor]
    return comp

  return sum(hand_comp(pair[:5]) > hand_comp(pair[5:]) for pair in pairs)

def mine():
  card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
  def card_rank(card):
    return card_ranks.index(card if len(card)==1 else card[:1])

  high_repeated_card = lambda hand,count: max(filter(lambda a: hand.count(a)==count, list(hand)), key=lambda a: card_ranks.index(a))

  hand_ranks = ['high_card', 'one_pair', 'two_pairs', 'three_of_a_kind', 'straight', 'flush', 'full_house', 'four_of_a_kind', 'straight_flush', 'royal_flush']
  def hand_rank(hand_key):
    return hand_ranks.index(hand_key)

  def hand_info(cards):
    hand = ''.join(sorted([c[:-1] for c in cards], key=lambda a: card_ranks.index(a)))
    suits = ''.join(sorted([c[-1] for c in cards]))
    if hand == 'TJQKA' and len(set(list(suits)))==1:
      return 'royal_flush',None,hand
    elif any(hand==card_ranks[i:i+5] for i in range(len(card_ranks)-5)) and len(set(list(suits)))==1:
      return 'straight_flush',hand[-1],hand
    hand_counts = dict((k,hand.count(k)) for k in list(hand) if hand.count(k))
    if len(set(list(hand))) == 2:
      if 4 in hand_counts.values():
        return 'four_of_a_kind',high_repeated_card(hand,4),hand
      if 3 in hand_counts.values():
        return 'full_house',high_repeated_card(hand,3),hand
    elif len(set(list(suits))) == 1:
      return 'flush',hand[-1],hand
    elif any(list(hand)==card_ranks[i:i+5] for i in range(len(card_ranks)-5+1)):
      return 'straight',hand[-1],hand
    elif any(len(set(list(hand[i:i+3]))) == 1 for i in range(len(hand)-3+1)):
      return 'three_of_a_kind',high_repeated_card(hand,3),hand
    elif len(set(list(hand))) == 3:
      return 'two_pairs',high_repeated_card(hand,2),hand
    elif len(set(list(hand))) == 4:
      return 'one_pair',high_repeated_card(hand,2),hand
    else:
      return 'high_card',hand[-1],hand

  def parse(line):
    cards = line.strip().split(' ')
    return (cards[:5], cards[5:])

  def player_1_win(h1,h2):
    if hand_rank(h1[0]) > hand_rank(h2[0]):
      return True
    elif hand_rank(h1[0]) == hand_rank(h2[0]):
      if card_rank(h1[1]) > card_rank(h2[1]):
        return True
      elif card_rank(h1[1]) == card_rank(h2[1]):
        i = 1
        while h1[2][-i] == h2[2][-i]:
          i +=1
        if card_rank(h1[2][-i]) > card_rank(h2[2][-i]):
          return True
    return False

  with open('problem054_poker.txt', 'r') as f:
    p1_wins = 0
    for l in f:
      p1,p2 = parse(l)
      h1,h2 = hand_info(p1), hand_info(p2)
      #print h1,h2
      if player_1_win(h1,h2):
        p1_wins += 1
      else:
        pass
  return p1_wins

#print "\nplayer 1 wins: %d" % mine()
print "\nplayer 1 wins: %d" % smart()
print "time: %f s" % (time.time() - t)