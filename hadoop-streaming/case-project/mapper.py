#!/usr/local/bin/python

import sys

def project(row):
    return row[2]

for line in sys.stdin:
    words = line.strip().split("\t")
    print(project(words))
