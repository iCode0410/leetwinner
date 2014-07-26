#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/reverse-integer/
[Detail]
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

[Func in leetcode]
class Solution:
    # @return an integer
    def reverse(self, x):
'''

from games import Game

class Game7(Game):

    def get_test_data(self):
        return [123, -123]

def jason_solver((x)):
    neg = False
    if x < 0 : neg, x = True, -x
    ret = 0
    while x / 10:
        ret = ret * 10+ x % 10
        x = x / 10
    ret = ret * 10 + x
    if ret > 0x7fffffff: return 0
    if neg: return -int(ret)
    return int(ret)

def iCode_solver((x)):
	for i in xrange(10000):
		pass

game7 = Game7(7, 'Reverse Integer', 'https://oj.leetcode.com/problems/reverse-integer/')
game7.add_solver(jason_solver, 'Jason')
game7.add_solver(iCode_solver, 'iCode')