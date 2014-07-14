#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Jasonwbw@yahoo.com

class Rewriter(object):

    def __init__(self, fo, readme_fheader = './README_Header.md'):
        self._write_header(readme_fheader, fo)

    def _write_header(self, readme_fheader, fo):
        with open(readme_fheader, 'r') as fp:
            for line in fp:
                fo.write(line)
        fo.write('##题目及胜者\n\n')
        fo.flush()

    def rewrite_onerecord(self, winner_name, game_num, game_name, game_link, fo):
        fo.write("* game " + str(game_num) + " : [" + game_name + "](" + game_link + ")'s winner is " + winner_name + "  \n")
        fo.flush()

    def rewrite_winner(self, finalwinner, num, total, fo):
        fo.write('\n##最终胜者\n\n')
        fo.write(finalwinner + ' with win ' + str(num) + ' in total ' + str(total) + ' games.  \n')

if __name__ == '__main__':
    pass