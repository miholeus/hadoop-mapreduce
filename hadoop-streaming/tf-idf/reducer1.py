#!/usr/local/bin/python

import sys

(lastKey, sumEl) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        (word, docnum) = lastKey.split("#")
        print(word + "\t" + docnum + "\t" + str(sumEl))
        (lastKey, sumEl) = (key, int(value))
    else:
        (lastKey, sumEl) = (key, sumEl + int(value))
if lastKey:
    (word, docnum) = lastKey.split("#")
    print(word + "\t" + docnum + "\t" + str(sumEl))
