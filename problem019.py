#!/usr/bin/env python
#
# The Euler Project: problem 19
#
# How many Sundays fell on the first of the month during the 
# twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime

t = datetime.timedelta(days=7)
d0 = datetime.datetime(day=1, month=1, year=1901)
dn = datetime.datetime(day=31, month=12, year=2000)

while d0.isoweekday() != 7:
  d0 += datetime.timedelta(days=1)

i = 0
d = d0
while d < dn:
  if d.isoweekday() == 7 and d.day == 1:
    i += 1
  d += t

print i
