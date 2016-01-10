#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: join2_reducer.py
Description: Reducer function.
"""
import sys

prev_tv_show = ""
flag = False
curr_tot_count = 0

for line in sys.stdin:
    line = line.strip()
    curr_tv_show, value = line.split('\t')

    if curr_tv_show != prev_tv_show:
        if flag:
            print('{0} {1}'.format(prev_tv_show, curr_tot_count))
        flag = False
        curr_tot_count = 0

    prev_tv_show = curr_tv_show

    if value.isdigit():
        curr_tot_count += int(value)
    else:
        flag = True

if flag:
    print('{0} {1}'.format(prev_tv_show, curr_tot_count))
