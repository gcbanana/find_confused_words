#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/5/11 22:09
# Description: 发现混淆词主文件


from match.match import Match, PinyinLevel
from find_words.find_words import FindWords


corpus = []
with open('data/sentences.txt', 'r', encoding='utf-8') as f:
    for line in f:
        corpus.append(line.strip())


find_words_obj = FindWords(corpus=corpus,
                           top_k=500,
                           chunk_size=10000,
                           min_n=3,
                           max_n=5,
                           min_freq=10)
find_words_obj.find_new_words()
find_words_obj.to_file(my_list=find_words_obj.new_words, file_path='data/new_words.txt')


match_obj = Match(build_words_path='data/new_words.txt', input_words_path='data/new_words.txt')
print(match_obj.match_all())
# [('婚贝请柬', '婚贝请间'), ('黑马矿友', '黑码矿友'), ('填锐绿盾', '天锐绿盾'), ... ]


# 开放拼音相似，懒得再生成，直接在new_words.txt中写入'杜拉拉'、'非马宽友'测试
new_word_out = open('data/new_words.txt', 'a+', encoding='utf-8')
new_word_out.write('杜拉拉' + '\n')
new_word_out.write('非马宽友')
new_word_out.close()
match_obj = Match(build_words_path='data/new_words.txt', input_words_path='data/new_words.txt',
                  level=PinyinLevel.CONFUSED)
print(match_obj.match('黑马矿友'))
print(match_obj.match_all())
# [('土拉拉', '杜拉拉'), ('黑马矿友', '非马宽友'), ('填锐绿盾', '天锐绿盾'), ... ]
