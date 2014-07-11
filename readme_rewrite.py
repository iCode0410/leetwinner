#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

class Rewriter(object):

    def __init__(self):
        self.fo = open('./README.md', 'w')
        self._write_header()

    def _write_header(self):
        with open('./README_Header.md', 'r') as fp:
            for line in fp:
                self.fo.write(line)
        self.fo.write('##题目及胜者\n\n')

    def rewrite_onerecord(self, winner_name, game_num, game_name, game_link):
        self.fo.write("* game " + str(game_num) + " : [" + game_name + "](" + game_link + ")'s winner is " + winner_name + "  \n")

    def close(self):
        self.fo.close()

if __name__ == '__main__':
    pass