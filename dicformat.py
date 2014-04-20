#!/usr/bin/env python
#-*- coding: utf-8 -*

import argparse
import re
import codecs

# 引数設定
parser = argparse.ArgumentParser()
parser.add_argument("in_path")
parser.add_argument("out_path")

if __name__ == '__main__':
    args = parser.parse_args()
    f_in = codecs.open(args.in_path, "r", "utf-8")
    f_out = codecs.open(args.out_path, "w", "utf-8")

    # 辞書フォーマットにそろえる
    for line in f_in:
        words = [re.sub(r'"$', '', re.sub(r'^"', '', w)) for w in line.split(',')]
        # パースが正しく行われていないとき，対象単語が1文字のときは無視
        if len(words) < 3 or len(words[1]) < 2 or len(words[2]) == 0:
            continue
        # 曖昧さ回避のための括弧は除外
        word = re.sub(r'\(.+\)$', '', words[1])
        reading = words[2]
        cost = int(max(-10000, 4800-400*len(word)**2))
        f_out.write(u"%s,*,*,%d,名詞,一般,*,*,*,*,%s,%s\n" % (word, cost, reading, reading))

    f_in.close()
    f_out.close()