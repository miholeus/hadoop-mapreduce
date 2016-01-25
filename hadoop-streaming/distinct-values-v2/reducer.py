#!/usr/local/bin/python

import sys
from collections import OrderedDict

storage = OrderedDict()
fvalues = list()
lastF = None

def sum_total(vals):
    global storage
    for val in vals:
        storage[val] = storage.get(val, 0) + 1

for line in sys.stdin:
    term = line.strip().split("\t")
    f = term[0]
    category = term[1]
    if lastF and lastF != f:
        # calculate counters
        sum_total(fvalues)
        fvalues = list()
    if category not in fvalues:
        fvalues.append(category)
    lastF = f
if fvalues:
    # calculate counters
    sum_total(fvalues)
for cat, cnt in storage.items():
    print(cat + "\t" + str(cnt))
