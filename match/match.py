#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/5/10 19:26
# Description: 匹配混淆词对


import pypinyin
from pypinyin import pinyin
from pygtrie import CharTrie


class Match(object):
    """匹配混淆词类"""

    def __init__(self, build_words_path, input_words_path):
        self.build_words_path = build_words_path
        self.input_words_path = input_words_path
        self.build_words = self.read_data(self.build_words_path)
        self.input_words = self.read_data(self.input_words_path)
        self._build_tree(self.build_words)

    @staticmethod
    def read_data(file_path):
        """
        读取数据
        :param file_path:
        :return: list
        """
        res = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                res.append(line.strip())
        return res

    def _build_tree(self, words):
        """
        构建trie树
        :param words:
        :return:
        """
        prefix_tree = CharTrie()
        for seq in words:
            py_str = ''.join([item[0] for item in pinyin(seq, style=pypinyin.NORMAL)])
            if py_str in prefix_tree:
                prefix_tree[py_str].append(seq)
            else:
                prefix_tree[py_str] = [seq]
        self.tree = prefix_tree

    def match(self, word, equal_length=True):
        """
        匹配word的混淆词
        :param word:
        :param equal_length: 只匹配等长的string
        :return:
        """
        res = []
        py = ''.join([item[0] for item in pinyin(word, style=pypinyin.NORMAL)])
        k, v = self.tree.longest_prefix(py)
        for item in v:
            if item != word:
                if equal_length and len(item) == len(word):
                    res.append(item)
                elif not equal_length:
                    res.append(item)
        return res

    def match_all(self, equal_length=True):
        """
        匹配整个文件(input words)
        :param equal_length:
        :return:
        """
        res = []
        for word in self.input_words:
            match_res = self.match(word, equal_length)
            for item in match_res:
                if (word, item) not in res and (item, word) not in res:
                    res.append((word, item))
        return res


if __name__ == '__main__':
    match_obj = Match(build_words_path='../data/new_words.txt',
                      input_words_path='../data/new_words.txt')
    print(match_obj.match(word='船老搬'))
    print(match_obj.match_all())
