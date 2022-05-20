#!/usr/bin/python3

import sys
from pprint import pprint

with open(sys.argv[1], 'r') as f:
  lines = f.readlines()

pprint(lines[:10])

lines = [l for l in lines if l != '\n']

depth = 1
lines2 = []
for l in lines:
  l = l.lstrip(' ')
  if l.startswith('*'):
    lines2.append('\n')
    depth = 0
    while l[depth] == '*':
      depth+=1
  l = '    ' * (depth-1) + l
  lines2.append(l)

pprint(lines2[:10])

with open(sys.argv[2], 'w') as f:
  f.write(''.join(lines2))

