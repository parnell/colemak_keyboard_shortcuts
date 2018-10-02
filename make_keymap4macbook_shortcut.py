#!/usr/bin/env python3

import re,os,sys

rhand = "jluyhneiokm"
lhand = "qwfpgarstdzxcvb"
# lhand = "qwertasdfgzxcvb"
# rhand = "yuiophjklnm"
qwerty = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
colemak = "qwfpgjluy;[]\\arstdhneio'zxcvbkm,./"

c2q = {}
q2c = {}

kcode = {} # karabiner key code 

for i in range(len(qwerty)):
  c2q[colemak[i]] = qwerty[i]
  q2c[qwerty[i]] = colemak[i]
  c2q[colemak[i].upper()] = qwerty[i].upper()
  q2c[qwerty[i].upper()] = colemak[i].upper()


prepend = "KeyCode::"
shift = "ModifierFlag::SHIFT_L"
def getKey(key):
    if key in kcode:
        return prepend+kcode[key]
    else:
        if key.isupper():
            return prepend+key.upper() + ","+shift
        return prepend+key.upper()


def init_karabiner_code():
    kcode['.'] = "KEYPAD_DOT"
    kcode['{'] = "BRACKET_LEFT,ModifierFlag::SHIFT_L"
    kcode['}'] = "BRACKET_RIGHT,ModifierFlag::SHIFT_L"
    kcode['/'] = "SLASH"
    kcode['\\'] = "BACKSLASH"
    kcode[' '] = "SPACE"
    kcode[';'] = "SEMICOLON"

def makeShortcut(shortcut_keys, shortcut, rcommand = True, name = None):
    keys = []
    if rcommand:
        keys.append("KeyCode::COMMAND_R")
    # shortcut_keys = oshortcut_keys.upper()
    # shortcut = oshortcut.upper()
    if not name:
        name = "'%s' to '%s' shortcut binding" %(shortcut_keys.lower(),shortcut.lower())

    id = "code.shortcut.%s" %(shortcut.lower())
    header = """
      <item>
        <name>@name</name>
        <identifier>@identifier</identifier>
        <autogen>
          __SimultaneousKeyPresses__
          @begin
    """.replace("@identifier", id).replace("@name",name)

    mid = """
          @end
          @begin
    """
    footer = """
          @end    
         </autogen>
         </item>
    """

    print(header)
    for c in shortcut_keys:
        # print ("----------    " + c2q[c] +" ---- " + c)
        keys.append(getKey(c2q[c] if c in c2q else c))
    
    print("         " + ",".join(keys))

    print(mid)
    keys = []
    for c in shortcut:
        keys.append(getKey(c2q[c] if c in c2q else c))
    print("         " +",".join(keys))
    print(footer)

init_karabiner_code()
makeShortcut( "pu", "Public")
makeShortcut("be", "\\begin{enumerate} \\end{enumerate}")
makeShortcut("se", "\\section{}")
makeShortcut("su", "\\subsection{}")
makeShortcut("sb", "\\subsubsection{}")
makeShortcut("pa", "\\paragraph{}")
makeShortcut("sp", "\\subparagraph{}")
