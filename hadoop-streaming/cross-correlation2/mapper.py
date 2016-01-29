#!/usr/local/bin/python

import sys

for line in sys.stdin:
    words = line.strip().split(" ")
    for i in words:
        h = dict()
        for j in words:
            if i != j:
                h[j] = h.get(j, 0) + 1
        string = i + "\t"
        for w,cnt in h.items():
            string += "%s:%s," % (w, str(cnt))
        string = string[:-1]
        print(string)
