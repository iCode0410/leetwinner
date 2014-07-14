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

def benchmark_game2(counter):
    from game2 import game2
    faster = None
    counter.add_users(game2.get_solver_users())
    for i in xrange(game2.total_solver()):
        game2.goto_next()
        t = timeit.Timer("game2.run()", "from game2 import game2")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game2.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game2.game_num, game2.game_name, game2.game_link, fo)
    return counter

def benchmark_game3(counter):
    from game3 import game3
    faster = None
    counter.add_users(game3.get_solver_users())
    for i in xrange(game3.total_solver()):
        game3.goto_next()
        t = timeit.Timer("game3.run()", "from game3 import game3")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game3.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game3.game_num, game3.game_name, game3.game_link, fo)
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