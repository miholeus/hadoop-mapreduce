#!/usr/local/bin/python
import sys

storage = dict()
for line in sys.stdin:
    for token in line.strip().split(" "):
        if token:
            storage[token] = storage.get(token, 0) + 1
for term, value in storage.items():
    print(term + "\t" + str(value))
