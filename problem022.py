#!/usr/bin/env python
#
# The Euler Project: problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
# containing over five-thousand first names, begin by sorting it into alphabetical 
# order. Then working out the alphabetical value for each name, multiply this value 
# by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is 
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain 
# a score of 938  53 = 49714.
#
# What is the total of all the name scores in the file?

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def score(name):
  return sum((alpha.index(s)+1) for s in name)

f = open('problem022_names.txt', 'r')
names = [n.strip('"') for n in f.read().split(',')]
names.sort()

print "Colin example"
print score(names[937]), names[937]

print "total", sum(score(name)*(index+1) for index,name in enumerate(names))