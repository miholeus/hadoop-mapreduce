#!/usr/local/bin/python

import sys

(lastKey, sumEl) = (None, list())
pStr = "{key}#{doc}\t{tf}\t{sum}"
storage = list()

for line in sys.stdin:
    (key, valueText) = line.strip().split("\t")
    (docnum, tf, value) = valueText.split(";")
    if lastKey and lastKey != key:
        for item in storage:
            print(pStr.format(key=lastKey, doc=item[0], tf=item[1], sum=len(sumEl)))
        sumEl = list()
        storage = list()
    sumEl.append(docnum)
    storage.append((docnum, tf))
    lastKey = key
if lastKey:
    for item in storage:
        print(pStr.format(key=lastKey, doc=item[0], tf=item[1], sum=len(sumEl)))
