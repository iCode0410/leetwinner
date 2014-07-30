#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/palindrome-number/
[Detail]
Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

[Func in leetcode]
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
'''

from games import Game

class Game9(Game):

    def get_test_data(self):
        return [1001, 10]

def jason_solver((x)):
    if x < 0: return False
    len = 0
    while x / (10 ** len) != 0:
        len += 1
    for i in xrange(len / 2):
        if x / 10 ** (len - 1 - i) % 10 != (x % 10 ** (i + 1)) / 10 ** i :
            return False
    return True

def iCode_solver((x)):
	for i in xrange(10000):
		pass

game9 = Game9(9, 'Palindrome Number', 'https://oj.leetcode.com/problems/palindrome-number/')
game9.add_solver(jason_solver, 'Jason')
game9.add_solver(iCode_solver, 'iCode')