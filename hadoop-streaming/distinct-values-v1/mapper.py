#!/usr/local/bin/python
import sys

for line in sys.stdin:
    words = line.strip().split("\t")
    f = words[0]
    g = words[1]
    garr = g.split(",")
    for gitem in garr:
        print(f + "," + gitem + "\t1")
