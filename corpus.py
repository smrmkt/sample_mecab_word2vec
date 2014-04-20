#!/usr/bin/env python
#-*- coding: utf-8 -*

import argparse
from lib.Parser import Parser
from lib.Vectorizer import Vectorizer

# 引数設定
parser = argparse.ArgumentParser()
parser.add_argument('menu')
parser.add_argument('in_path')
parser.add_argument('out_path', nargs='?')

def get_input():
    pos = []
    neg = []
    for l in raw_input('\nplease input formula(or "END"): ').split('+'):
        words = l.split('-')
        pos.append(words[0])
        for i in range(1, len(words)):
            neg.append(words[i])
    return pos, neg

if __name__ == '__main__':
    args = parser.parse_args()
    menu = args.menu
    in_path = args.in_path
    out_path = args.out_path

    if menu == 'parse':
        p = Parser('-Owakati')
        p.parse_file(in_path, out_path)
    elif menu == 'vectorize':
        v = Vectorizer(min_count=10)
        v.build_from_file(in_path)
        v.store(out_path)
    elif menu == 'calc':
        v = Vectorizer()
        v.load(in_path)
        while True:
            pos, neg = get_input()
            if pos[0] == 'END':
                break;
            else:
                v.calc(pos, neg)
