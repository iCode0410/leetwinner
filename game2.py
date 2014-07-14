#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

'''
[Link] 
https://oj.leetcode.com/problems/median-of-two-sorted-arrays/

[Detail]
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

[Func in leetcode]
# @return a float
def findMedianSortedArrays(self, A, B):
'''

from games import Game

class Game2(Game):

	def get_test_data(self):
		return [([1, 2, 5, 7, 9], [2, 5, 8, 11]), ([15, 120], [2, 5, 8, 11])]

def jason_solver((num, target)):
	snum = sorted(num)
	i, j = 0, len(snum) - 1
	while i < j:
		if snum[i] + snum[j] > target:
			j -= 1
		elif snum[i] + snum[j] < target:
			i += 1
		else:
			i1, i2 = num.index(snum[i]), num.index(snum[j])
			if i1 == i2:
				i2 = num[i1 + 1:].index(snum[i]) + i1 + 1
			return (min(i1, i2) + 1, max(i1, i2) + 1)
	return None

def jason_getMedian(A, B, k):
    if len(A) > len(B): return jason_getMedian(B, A, k)
    if len(A) == 0: return B[k-1]
    if k == 1: return min(A[0], B[0])
    ma, mb = min(k/2, len(A)), k - min(k/2, len(A))
    if A[ma - 1] > B[mb - 1]:
        return jason_getMedian(A, B[mb:], k - mb)
    return jason_getMedian(A[ma:], B, k - ma)
     
def jason_solver((A, B)):
    if (len(A) + len(B)) % 2 == 1: 
        return jason_getMedian(A, B, (len(A) + len(B)) / 2 + 1)
    else:
        return 0.5 * ( jason_getMedian(A, B, (len(A) + len(B)) / 2) + jason_getMedian(A, B, (len(A) + len(B)) / 2 + 1) )

def iCode_solver((A, B)):
	for i in xrange(10000):
		pass

game2 = Game2(2, 'Median of Two Sorted Arrays', 'https://oj.leetcode.com/problems/median-of-two-sorted-arrays/')
game2.add_solver(jason_solver, 'Jason')
game2.add_solver(iCode_solver, 'iCode')