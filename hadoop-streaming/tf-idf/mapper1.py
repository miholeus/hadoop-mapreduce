#!/usr/local/bin/python

import sys
import re

rWords = re.compile(u'\w+', re.UNICODE)

for line in sys.stdin:
    text = line.strip()
    t = rWords.findall(text)
    docnum = t[0]
    words = t[1:]

    for word in words:
        if word:
            print(word+"#"+docnum+"\t1")
