#!/usr/bin/python

from collections import Counter
with open('apache_access.log') as inputfile:
    count = Counter(line.split('-', 1)[0].strip() for line in inputfile)

print count.most_common(10)