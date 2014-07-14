#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

import timeit
import time
from readme_rewrite import Rewriter
from winner_counter import WinnerCounter

loops = 1000

fo = open('./README.md', 'w')
rewriter = Rewriter(fo)

def benchmark_game1(counter):
    from game1 import game1
    faster = None
    counter.add_users(game1.get_solver_users())
    for i in xrange(game1.total_solver()):
        game1.goto_next()
        t = timeit.Timer("game1.run()", "from game1 import game1")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game1.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game1.game_num, game1.game_name, game1.game_link, fo)
    return counter

def final(counter, total):
    finalwinner, num = counter.final_winner()
    rewriter.rewrite_winner(finalwinner, num, total, fo)
    return counter

if __name__ == '__main__':
    import benchmarks as b
    counter = WinnerCounter()
    total = 0
    for func_name, func in  b.__dict__.items():
        if func_name.startswith('benchmark_'):
            counter = func(counter)
            total += 1
    for func_name, func in  b.__dict__.items():
        if func_name == 'final':
            func(counter, total)
    fo.close()