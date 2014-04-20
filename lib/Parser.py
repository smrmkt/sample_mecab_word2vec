#!/usr/bin/env python
#-*- coding: utf-8 -*

"""
MeCabのラッパー
"""

import MeCab

class Parser:

    def __init__(self, option=''):
        self._mecab = MeCab.Tagger(option)

    def parse_file(self, in_path, out_path):
        raw = open(in_path, 'r')
        parsed = open(out_path, 'w')
        for l in raw:
            p = self.parse(l)
            if p is not None:
                parsed.write(p)
        raw.close()
        parsed.close()


    def parse(self, sentences, debug=False):
        p = self._mecab.parse(sentences)
        if debug is True:
            print p
        return p
