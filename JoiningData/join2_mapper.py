#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: join2_mapper.py
Email: i(at)huxuan.org
Description: Mapper function.
"""
import sys

for line in sys.stdin:
    tv_show, value = line.split(',')
    tv_show = tv_show.strip()
    value = value.strip()

    if value.isdigit() or value == 'ABC':
        print('{0}\t{1}'.format(tv_show, value))
