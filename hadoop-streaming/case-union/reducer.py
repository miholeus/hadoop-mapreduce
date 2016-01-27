#!/usr/local/bin/python

import sys

lastKey = None

for line in sys.stdin:
    words = line.strip().split("\t")
    if words[0] != lastKey:
        print(words[0])
    lastKey = words[0]
