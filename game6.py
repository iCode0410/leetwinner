#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/zigzag-conversion/
[Detail]
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

[Func in leetcode]
class Solution:
    # @return a string
    def convert(self, s, nRows):
'''

from games import Game

class Game6(Game):

    def get_test_data(self):
        return [('ABC', 1), ('AB', 2), ('ABC', 2), ("ABCDE", 2)]

def jason_solver((s, nRows)):
    if s == None or s == '' or nRows == 1: return s
    res, group_n = '', nRows + (nRows - 2)
    for i in xrange(nRows):
        for j in xrange(i, len(s), group_n):
            res += s[j]
            x = group_n - i * 2
            if x > 0 and x < group_n and j + x < len(s):
                res += s[j + x]
    return res

def iCode_solver((s, nRows)):
	for i in xrange(10000):
		pass

game6 = Game6(6, 'ZigZag Conversion', 'https://oj.leetcode.com/problems/zigzag-conversion/')
game6.add_solver(jason_solver, 'Jason')
game6.add_solver(iCode_solver, 'iCode')