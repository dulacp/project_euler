#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 59
#
# Each character on a computer is assigned a unique code and the preferred standard is ASCII 
# (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, 
# and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with 
# a given value, taken from a secret key. The advantage with the XOR function is that using the same 
# encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up 
# of random bytes. The user would keep the encrypted message and the encryption key in different locations, 
# and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as 
# a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout 
# the message. The balance for this method is using a sufficiently long password key for security, but short 
# enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt 
# (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that 
# the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the 
# original text.

from decorators import benchmark

@benchmark
def solve():
  # lower case ascii codes
  ascii = [ord(s) for s in 'abcdefghijklmnopqrstuvwxyz']
  # fifty most common words [http://en.wikipedia.org/wiki/Most_common_words_in_English]
  common_english_words = ['the','be''to','of','and','a''in','that','have','I','it','for','not','on','with','he',\
    'as','you','do','at','this','but','his','by','from','they','we','say','her','she','or','an','will','my','one','all',\
    'would','there','their','what','so','up','out','if','about','who','get','which','go','me']

  def sounds_like_english(decoded):
    """affect a score to the likelihood that it is english words"""
    tokens = decoded.split(' ')
    if len(tokens) < 10:
      return 0
    return len(set(tokens).intersection(common_english_words))

  def decode_from_ascii(coded_ascii):
    return ''.join([unichr(a) for a in coded_ascii])

  def decrypt(crypted, key_ascii):
    N = len(key_ascii)
    return [a^key_ascii[i%N] for i,a in enumerate(crypted)]

  with open('problem059_cipher1.txt') as f:
    crypted_ascii = map(int, f.read().split(','))
    for x in ascii:
      for y in ascii:
        for z in ascii:
          d = decrypt(crypted_ascii, [x,y,z])
          dd = decode_from_ascii(d)
          #print dd
          #raw_input()
          if sounds_like_english(dd) > 10:
            print dd
            print "the key is :", decode_from_ascii([x,y,z])
            return sum(d)

if __name__ == "__main__":
  solve()