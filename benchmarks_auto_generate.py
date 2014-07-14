#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

def load_and_write(filename, fo, func = None):
    with open(filename, 'r') as fp:
        for line in fp:
            if func != None:
                fo.write(func(line))
            else:
                fo.write(line)

if __name__ == '__main__':
    import os
    import re
    fo = open('./benchmarks.py', 'w')
    load_and_write('./benchmarks.py.header', fo)
    filelist = os.listdir('./')
    for filename in filelist:
        if re.search('game[0-9]+.py$', filename):
            func = lambda x : x.replace('game1', filename.replace('.py', ''))
            load_and_write('./benchmarks.py.body', fo, func = func)
            fo.write('\n')
    load_and_write('./benchmarks.py.footer', fo)
    fo.close()
