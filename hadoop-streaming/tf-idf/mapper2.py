#!/usr/local/bin/python

import sys

for line in sys.stdin:
    text = line.strip().split("\t")
    print(text[0] + "\t" + text[1]+";"+text[2]+";1")
