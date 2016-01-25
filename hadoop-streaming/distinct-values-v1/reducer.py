#!/usr/local/bin/python
import sys

lastPair = None

for line in sys.stdin:
    words = line.strip().split("\t")
    pair = words[0]
    if pair != lastPair:
        lastPair = pair
        print(pair)
