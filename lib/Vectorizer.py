#!/usr/bin/env python
#-*- coding: utf-8 -*

"""
word2vecのラッパー
"""

import logging
import gensim
from gensim.models import word2vec

class Vectorizer:

    def __init__(self, min_count=1, size=100, logger=True):
        if logger is True:
            logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        self._model = gensim.models.Word2Vec(min_count=min_count, size=size)

    def build(self, sentences):
        self._model.build_vocab(sentences)

    def build_from_file(self, path):
        sentences = word2vec.Text8Corpus(path)
        self._model.build_vocab(sentences)

    def store(self, path):
        self._model.save(path)

    def load(self, path):
        self._model = gensim.models.Word2Vec.load(path)

    def calc(self, plus, minus=[], n=5):
        try:
            result = self._model.most_similar(positive=plus, negative=minus, topn=n)
            for r in result:
                print r[0], r[1]
        except KeyError, (message):
            print message