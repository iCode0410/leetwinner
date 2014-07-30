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

def benchmark_game4(counter):
    from game4 import game4
    faster = None
    counter.add_users(game4.get_solver_users())
    for i in xrange(game4.total_solver()):
        game4.goto_next()
        t = timeit.Timer("game4.run()", "from game4 import game4")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game4.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game4.game_num, game4.game_name, game4.game_link, fo)
    return counter

def benchmark_game6(counter):
    from game6 import game6
    faster = None
    counter.add_users(game6.get_solver_users())
    for i in xrange(game6.total_solver()):
        game6.goto_next()
        t = timeit.Timer("game6.run()", "from game6 import game6")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game6.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game6.game_num, game6.game_name, game6.game_link, fo)
    return counter

def benchmark_game7(counter):
    from game7 import game7
    faster = None
    counter.add_users(game7.get_solver_users())
    for i in xrange(game7.total_solver()):
        game7.goto_next()
        t = timeit.Timer("game7.run()", "from game7 import game7")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game7.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game7.game_num, game7.game_name, game7.game_link, fo)
    return counter

def benchmark_game8(counter):
    from game8 import game8
    faster = None
    counter.add_users(game8.get_solver_users())
    for i in xrange(game8.total_solver()):
        game8.goto_next()
        t = timeit.Timer("game8.run()", "from game8 import game8")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game8.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game8.game_num, game8.game_name, game8.game_link, fo)
    return counter

def benchmark_game9(counter):
    from game9 import game9
    faster = None
    counter.add_users(game9.get_solver_users())
    for i in xrange(game9.total_solver()):
        game9.goto_next()
        t = timeit.Timer("game9.run()", "from game9 import game9")
        t1 = t.timeit(number=loops)
        if faster == None or faster[0] > t1:
            faster = (t1, game9.currents_solvername())
    counter.count_winner(faster[1])
    rewriter.rewrite_onerecord(faster[1], game9.game_num, game9.game_name, game9.game_link, fo)
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