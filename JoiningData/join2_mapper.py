#!/usr/bin/env python
import sys
shows = []

for line in sys.stdin:
    line       = line.strip()
    key_value  = line.split(',')

    if key_value[1] == 'ABC':
        if key_value[1] not in shows:
            shows.append(key_value[0])

    if key_value[1].isdigit() and (key_value[0] in shows):
        print('{0}\t{1}'.format(key_value[0], key_value[1]) )
