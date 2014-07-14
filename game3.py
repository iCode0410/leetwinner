#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

[Detail]
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

[Func in leetcode]
# @return an integer
def lengthOfLongestSubstring(self, s):
'''

from games import Game

class Game3(Game):

	def get_test_data(self):
		return [('sdfsdfsafwefbvdfhtrge'), ('dsegrehrtyewrtq')]

def jason_solver((s)):
    if s == None : return 0
    max_len, current_len, i = 0, 0, 0
    indexs = {}
    while i < len(s):
        if s[i] not in indexs:
            current_len += 1
        else:
            if current_len > max_len: max_len = current_len
            for j in xrange(i - current_len, indexs[s[i]]): del indexs[s[j]]
            current_len -= (current_len - (i - indexs[s[i]]))
        indexs[s[i]] = i
        i += 1
    if current_len > max_len: max_len = current_len
    return max_len

def iCode_solver((s)):
	for i in xrange(10000):
		pass

game3 = Game3(3, 'Longest Substring Without Repeating Characters ', 'https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/')
game3.add_solver(jason_solver, 'Jason')
game3.add_solver(iCode_solver, 'iCode')