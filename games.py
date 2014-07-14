#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# games are sorted by time
#
# Jasonwbw@yahoo.com

from abc import ABCMeta, abstractmethod

class Game(object):

    __metaclass__ = ABCMeta

    def __init__(self, game_num, game_name, game_link, solvers = [], solver_names = []):
        self.game_num = game_num
        self.game_name = game_name
        self.game_link = game_link
        self.solvers = [(solvers[i], solver_names[i]) for i in xrange(len(solvers))]
        self.index = -1

    def get_solver_users(self):
        return [user for solver, user in self.solvers]

    def add_solver(self, func, nickname):
        self.solvers.append((func, nickname))

    def total_solver(self):
        return len(self.solvers)

    def currents_solvername(self):
        return self.solvers[self.index][1]

    def goto_next(self):
        self.index += 1

    def run(self):
        for test in self.get_test_data():
            self.solvers[self.index][0](test)

    @abstractmethod
    def get_test_data(self):
        pass