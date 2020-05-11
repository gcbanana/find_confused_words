#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/5/10 15:30
# Description: 新词发现


from smoothnlp.algorithm.phrase import extract_phrase


class FindWords(object):
    """新词发现"""

    def __init__(self, corpus, top_k, chunk_size, min_n, max_n, min_freq):
        self.corpus = corpus
        self.top_k = top_k
        self.chunk_size = chunk_size
        self.min_n = min_n
        self.max_n = max_n
        self.min_freq = min_freq
        self.new_words = None

    def find_new_words(self):
        """
        调用smooth nlp的接口，新词发现
        :return:
        """
        words = extract_phrase(corpus=self.corpus,
                               top_k=self.top_k,
                               chunk_size=self.chunk_size,
                               min_n=self.min_n,
                               max_n=self.max_n,
                               min_freq=self.min_freq)
        self.new_words = words

    @staticmethod
    def to_file(my_list, file_path):
        """
        将list写入文件
        :param my_list:
        :param file_path:
        :return:
        """
        out = open(file_path, 'w', encoding='utf-8')
        for item in my_list:
            out.write(item)
            out.write('\n')
        out.close()
