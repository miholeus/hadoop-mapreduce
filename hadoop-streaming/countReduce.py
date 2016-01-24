#!/usr/local/bin/python
import sys

(lastKey, sumEl) = (None, 0)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        print lastKey + "\t" + str(sumEl)
        (lastKey, sumEl) = (key, int(value))
    else:
        (lastKey, sumEl) = (key, sumEl + int(value))
if lastKey:
    print lastKey + "\t" + str(sumEl)
