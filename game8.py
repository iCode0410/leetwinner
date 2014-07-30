#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/string-to-integer-atoi/
[Detail]
String to Integer (atoi) 

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

[Func in leetcode]
class Solution:
    # @return an integer
    def atoi(self, str):
'''

from games import Game

class Game8(Game):

    def get_test_data(self):
        return ["    010", " b11228552307"]

def jason_solver((str)):
    if str == None or str.strip() == '' : return 0
    str = str.strip()
    b1, b2 = str[0] == '-' or str[0] == '+', str[0] <= '9' and str[0] >= '0'
    if not b1 and not b2: return 0
    start, news = 1 if b1 else 0, str[0] if b1 else ""
        
    for c in str[start:]:
        if c <= '9' and c >= '0': news += c
        else: break
    INT_MAX, INT_MIN = 2147483647, -2147483648
    try:
        value = int(news)
        if value > INT_MAX : return INT_MAX
        if value < INT_MIN : return INT_MIN
        return value
    except:
        return 0

def iCode_solver((str)):
	for i in xrange(10000):
		pass

game8 = Game8(8, 'String to Integer (atoi) ', 'https://oj.leetcode.com/problems/string-to-integer-atoi/')
game8.add_solver(jason_solver, 'Jason')
game8.add_solver(iCode_solver, 'iCode')