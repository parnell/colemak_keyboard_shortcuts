#!/usr/bin/env python3

import re,os,sys,uuid

# infile = sys.argv[1]

infile = "/Users/parnell/yadd/data/keyboard_code_shortcuts.txt"
# dictKey = """
# <dict>
# <key>abbreviation</key>
# <string>{1}</string>
# <key>abbreviationMode</key>
# <integer>0</integer>
# <key>creationDate</key>
# <date>{2}</date>
# <key>flags</key>
# <integer>0</integer>
# <key>label</key>
# <string>{1} -> {0}</string>
# <key>modificationDate</key>
# <date>{2}</date>
# <key>plainText</key>
# <string>{0}</string>
# <key>snippetType</key>
# <integer>0</integer>
# <key>useCount</key>
# <integer>0</integer>
# <key>uuidString</key>
# <string>{3}</string>
# </dict>
# """

dictKey = "{1},{0},{1} -> {0},{2},{3}"
# print("<array>")
for line in open(infile):
  line = line.strip()
  split = line.split(",")
  # print(line, split)
  if not line:
    continue

  word = split[0]
  abv = split[1].split("|")
  creationDate = split[2] if len(split) > 2 else "2014-02-04"
  flags = 0
  # print(word, abv,uuid)
  for ab in abv:
    id = str(uuid.uuid1())
    print(dictKey.format (word,ab,creationDate, id))

  # break
# print("</array>")