#!/usr/local/bin/python
import sys

(lastKey, value) = (None, 0)
storage = list()

def avg(storage):
    s = sum(storage)
    n = len(storage)
    return int(s/n)

for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if lastKey and lastKey != key:
        res = avg(storage)
        print(key + "\t" + str(res))
        storage = list()
        storage.append(int(value))
    else:
        storage.append(int(value))
    lastKey = key


if lastKey:
    res = avg(storage)
    print(lastKey + "\t" + str(res))
