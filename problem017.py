#!/usr/bin/env python
#
# The Euler Project: problem 17
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use 
# of "and" when writing out numbers is in compliance with British usage.

limit = 1000

en_map = {
  0: "",
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  100: "hundred",
  1000: "thousand"
}

def int2str(x):
  """
  Ecriture anglosaxone de l'entier x

  exemple: 
    >>> x = 321
    >>> int2str(x)
    three hundred and twenty one
  """
  s = ""
  x = int(x)
  if x/1000:
    s += en_map[x/1000] + " " + en_map[1000]
    x -= (x/1000)*1000
  if x and x/100:
    if s: s += " and "
    s += en_map[x/100] + " " + en_map[100]
    x -= (x/100)*100
  if x and x > 20 and x%10:
    if s: s += " and "
    s += en_map[x - x%10] + " " + en_map[x%10]
  elif x:
    if s: s += " and "
    s += en_map[x]
  return s.strip()

# test
test = [342, 100, 101, 115]
for t in test:
  print t
  print int2str(t)
  print int2str(t).replace(' ', '')
  print len(int2str(t).replace(' ', ''))
  print 

print sum(len(int2str(i).replace(' ', '')) for i in range(1,limit+1))