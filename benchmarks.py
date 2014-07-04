#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

import timeit
import time

loops = 1000

def benchmark_game1():
    from game1 import game1
    faster = None
    for i in xrange(game1.total_solver()):
        game1.goto_next()
        t = timeit.Timer("game1.run()", "from game1 import game1")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game1.currents_solvername())
    print 'winner for game1 is', faster[1]

if __name__ == '__main__':
    import benchmarks as b
    for func_name, func in  b.__dict__.items():
        if func_name.startswith('benchmark_'):
            func()