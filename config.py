#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/6/29 22:06
# Description: 读取配置


import yaml


INITIALS_FILE = 'pinyin/initials.yml'
FINALS_FILE = 'pinyin/finals.yml'


class Config(object):

    def __init__(self):
        self.initials_dict = self.load_pinyin_config(INITIALS_FILE)
        self.finals_dict = self.load_pinyin_config(FINALS_FILE)

    @staticmethod
    def load_pinyin_config(file):
        """
        加载拼音的配置文件
        :param file:
        :return:
        """
        return yaml.safe_load(open(file, 'r', encoding='utf-8'))


config_basic = Config()
