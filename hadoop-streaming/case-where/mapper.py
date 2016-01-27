#!/usr/local/bin/python

import sys

for line in sys.stdin:
    words = line.strip().split("\t")
    if words[1] == 'user10':
        print(line.strip())
