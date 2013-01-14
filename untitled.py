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


def equivalent(x):
  if x==0:
    return 0
  elif x==1:  #one
    return 3
  elif x==2:  #two
    return 3
  elif x==3:  #three
    return 5
  elif x==4:  #four
    return 4
  elif x==5:  #five
    return 4
  elif x==6:  #six
    return 3
  elif x==7:  #seven
    return 5
  elif x==8:  #eight
    return 5
  elif x==9:  #nine
    return 4
  elif x==10: #ten
    return 3
  elif x==11: #eleven
    return 6
  elif x==12: #twelve
    return 6
  elif x==13: #thirteen
    return 8
  elif x==14: #fourteen
    return 8  
  elif x==15: #fifteen
    return 7
  elif x==16: #sixteen
    return 7
  elif x==17: #seventeen
    return 9
  elif x==18: #eighteen
    return 8
  elif x==19: #nineteen
    return 8
  elif x==20: #twenty
    return 6
  elif x==30: #thirty
    return 6
  elif x==40: #forty
    return 5
  elif x==50: #fifty
    return 5  
  elif x==60: #sixty
    return 5
  elif x==70: #seventy
    return 7
  elif x==80: #eighty
    return 6
  elif x==90: #ninety
    return 6
  elif x==100: #one hundred
    return 10
  elif x==1000: #one thousand
    return 11
  
def decomp(x):
  if equivalent(x)==None:
    x_prime=str(x)
    longeur=len(x_prime)
    if x <= 20:
      return equivalent(x)
    elif longeur<=2:
      return equivalent(x%10)+equivalent(10*int(x_prime[0]))
    return equivalent(int(x_prime[0]))+equivalent(100)+decomp(x%100)-3+3
  else: 
    return equivalent(x)

# test 
for i in range(1,1001):
  if len(int2str(i).replace(' ', '')) != decomp(i):
    print "Erreur pour", i