#!/usr/bin/env python3

import re,os,sys

uletters = "qwfpgjluy"
# rhand = "jluyhneiokm" # Colemak
# lhand = "qwfpgarstdzxcvb" # Colemak

# rhand = "fgcrldhtnsbmwvz"  # Dvorak
# lhand = ",.pyaoeui;qjkx" # Dvorak

# lhand = "qwertasdfgzxcvb"
# rhand = "yuiophjklnm"

rgrep = "^["+uletters+"]+$"
# lgrep = "^["+lhand+"]+$"

# infile = sys.argv[-1]
infile = "/Users/parnell/workspace/data/english_wordlist.txt"
count =0
maxes = set()
ml =0
words = set()
for word in open(infile):
  count+=1
  # if count>100:
  #   break
  word = word.strip()
  if (len(word) <=1): 
    continue
  # print(word)
  # if (len(word) > 4 and re.match(rgrep,word)):
  if (re.match(rgrep,word)):
    if (len(word) > ml):
      maxes = set()
      ml = len(word)
    if (len(word)==ml):
      maxes.add(word)
    words.add(word)

for w in sorted(words):
  print(w)
print("max length", maxes)