#!/usr/local/bin/python

import sys

storage = {'query': list(), 'url': list()}
lastKey = None

def emit(storage):
    for query in storage['query']:
        for url in storage['url']:
            print(lastKey + "\t" + query + "\t" + url)

for line in sys.stdin:
    words = line.strip().split("\t")
    user_id, text = (words[0], words[1])
    marker, value = text.split(":")
    if lastKey and user_id != lastKey:
        # flush storage
        emit(storage)
        storage = {'query': list(), 'url': list()}
    lastKey = user_id
    storage[marker].append(value)
if lastKey and len(storage['query']) > 1 and len(storage['url']) > 1:
    emit(storage)
