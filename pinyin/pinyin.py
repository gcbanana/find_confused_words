#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/6/28 21:51
# Description: 拼音编码


from config import config_basic
from pypinyin import pinyin, Style


DEFAULT = '^'  # 默认通配符
PLACEHOLDER = '_'  # 无生母占位符


class Pinyin(object):

    def __init__(self):
        pass

    @staticmethod
    def is_chinese(char):
        """
        判断字符是否是中文
        :param char:
        :return:
        """
        if '\u4e00' <= char <= '\u9fff':
            return True
        else:
            return False

    def translate(self, word, level='confused'):
        """
        将词转化为拼音编码，例如：'拿捏' -> 'BaBk'
        :param word:
        :param level: 近似音开放的程度，配置文件里暂时只有confused
        :return:
        """
        code_list = []  # 存每个字符的编码
        initials_code_dict = config_basic.initials_dict[level]
        finals_code_dict = config_basic.finals_dict[level]

        for char in word:
            initial_code = initials_code_dict[DEFAULT]
            final_code = finals_code_dict[DEFAULT]

            if self.is_chinese(char):
                char_initial = pinyin(char, style=Style.INITIALS)
                char_final = pinyin(char, style=Style.FINALS)
                # 无声母现象，例如：'安'
                if char_initial == [['']]:
                    initial_code = initials_code_dict[PLACEHOLDER]
                else:
                    initial_code = initials_code_dict[char_initial[0][0]]

                final_code = finals_code_dict[char_final[0][0]]

            code_list.append(initial_code + final_code)

        return ''.join(code_list)


py_maker = Pinyin()
