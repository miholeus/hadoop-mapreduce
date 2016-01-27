#!/usr/local/bin/python

import sys

lastKey, values = (None, list())

for line in sys.stdin:
    words = line.strip().split("\t")
    if values and words[0] != lastKey:
        if len(values) == 1:
            if values[0] == 'A' or values[0] == 'B':
                print(lastKey)
        values = list() # flush storage
    values.append(words[1])
    lastKey = words[0]
if lastKey and len(values) == 1:
    if values[0] == 'A' or values[0] == 'B':
        print(lastKey)
