#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/two-sum/

[Detail]
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

[Func in leetcode]
# @return a tuple, (index1, index2)
def twoSum(self, num, target):
'''

from games import Game

class Game1(Game):

	def get_test_data(self):
		return [([2, 7, 11, 15], 9)]

def jason_solver((num, target)):
	for i in xrange(100):
		pass

def iCode_solver((num, target)):
	pass

game1 = Game1()
game1.add_solver(jason_solver, 'Jason')
game1.add_solver(iCode_solver, 'iCode')