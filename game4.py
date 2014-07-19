#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/add-two-numbers/
[Detail]
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

[Func in leetcode]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
'''

from games import Game

class Game4(Game):

    def get_test_data(self):
        l1_1, l2_1 = ListNode(2), ListNode(5)
        l1_1.next = ListNode(4)
        l1_1.next.next = ListNode(4)
        l2_1.next = ListNode(6)
        l2_1.next.next = ListNode(4)
        return [(l1_1, l2_1)]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def jason_solver((l1, l2)):
    if l1 is None: return l2
    if l2 is None: return l1
    header = ListNode((l1.val + l2.val) % 10)
    cursor, add = header, (l1.val + l2.val) / 10
    l1 = l1.next; l2 = l2.next
    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            cursor.next = ListNode((l1.val + l2.val + add) % 10)
            add = (l1.val + l2.val + add) / 10
        elif l1 is not None:
            cursor.next = ListNode((l1.val + add) % 10)
            add = (l1.val + add) / 10
        else:
            cursor.next = ListNode((l2.val + add) % 10)
            add = (l2.val + add) / 10
        cursor = cursor.next
        if l1 is not None: l1 = l1.next
        if l2 is not None: l2 = l2.next
    if add == 1:
        cursor.next = ListNode(1)
    return header

def iCode_solver((l1, l2)):
	for i in xrange(10000):
		pass

game4 = Game4(4, 'Add Two Numbers', 'https://oj.leetcode.com/problems/add-two-numbers/')
game4.add_solver(jason_solver, 'Jason')
game4.add_solver(iCode_solver, 'iCode')