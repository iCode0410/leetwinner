#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

class WinnerCounter(object):

    def __init__(self):
        self.users = []
        self.wincount = []

    def add_users(self, users):
        for user in users:
            self._add_user(user)

    def _add_user(self, username):
        if username not in self.users:
            self.users.append(username)
            self.wincount.append(0)
        return username

    def count_winner(self, username):
        if username not in self.users:
            return
        self.wincount[self.users.index(username)] += 1

    def final_winner(self):
        winners, max_count = [], 0
        for i in xrange(len(self.users)):
            if self.wincount[i] > max_count:
                winners = [self.users[i]]
                max_count = self.wincount[i]
            elif self.wincount[i] == max_count:
                winners.append(self.users[i])
        return ','.join(winners), max_count

if __name__ == '__main__':
    pass