#!/usr/local/bin/python
import sys

(lastKey, value) = (None, 0)
storage = {'values': list(), 'cnt': 0}
globalStorage = dict()

def avg(storage):
    return {'sum': sum(storage['values']), 'cnt': storage['cnt']}

for line in sys.stdin:
    (key, pairs) = line.strip().split("\t")
    value, cnt = pairs.split(";")
    if lastKey and lastKey != key:
        res = avg(storage)
        print(lastKey + "\t" + str(res['sum']) + ";" + str(res['cnt']))
        storage = {'values': list(), 'cnt': 0} #init new one, flush old
    lastKey = key
    storage['values'].append(int(value))
    storage['cnt'] += int(cnt)

if lastKey:
    res = avg(storage)
    print(lastKey + "\t" + str(res['sum']) + ";" + str(res['cnt']))
