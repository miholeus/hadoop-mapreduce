#!/usr/local/bin/python
import sys

for line in sys.stdin:
    words = line.strip().split(",")
    print(words[1] + "\t1")
