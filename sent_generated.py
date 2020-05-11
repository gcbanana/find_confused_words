#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Jeffrey Gao
# Time: 2020/5/8 22:17
# Description: 生成假预料


# 本脚本用来生成一些关于app名字的句子
# 1. 爬取一些app名字
# 2. 生成混淆app名字
# 3. 根据一些模板，以及拼音和汉字的转换，生成一些包含正确app名字和一些包含错误混淆app名字的句子
# 4. 写入文件


import json
import time
import random
import requests
from pypinyin import lazy_pinyin


# 1 借助小米的网页商店，爬10页app名字
base_url = 'http://app.mi.com/categotyAllListApi?'
page_num = 10
app_names = []
app_names_file = 'data/app_names.txt'


for i in range(page_num):
    params = {
        'page': str(i + 1),
        'categoryId': '5',
        'pageSize': '30'
    }
    data = requests.get(base_url, params)
    data.encoding = 'utf-8'
    data = json.loads(data.text)['data']
    for item in data:
        if item['displayName']:
            app_names.append(item['displayName'])
            print(item['displayName'])
    print('已爬取完第{}页...'.format(str(i + 1)))
    time.sleep(1)


# 爬取app名称写入文件
out_app_names = open(app_names_file, 'w', encoding='utf-8')
for item in app_names:
    out_app_names.write(item)
    out_app_names.write('\n')
out_app_names.close()


# 2
py_char_dict = dict()
app_names = []
confused_app_names = []
confused_app_names_file = 'data/confused_app_names.txt'
sentences_file = 'data/sentences.txt'


# 统计每个字的拼音，生成dict
with open(app_names_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        app_names.append(line)
        for char in line:
            py = lazy_pinyin(char, errors='ignore')
            if not py:
                pass
            else:
                py = py[0]
                if py in py_char_dict:
                    py_char_dict[py].append(char)
                else:
                    py_char_dict[py] = [char]


confused_app_num = 100
random.shuffle(app_names)
i = 1


# 生成100个错误app名，随机替换掉一个字
for app_name in app_names:
    modified_index = random.choice(range(len(app_name)))
    py = lazy_pinyin(app_name[modified_index])
    if py and py[0] in py_char_dict and len(app_name) <= 4:
        modified_char = random.choice(py_char_dict[py[0]])
        modified_name = app_name[:modified_index] + modified_char + app_name[modified_index + 1:]
        if modified_name != app_name:
            confused_app_names.append(modified_name)
            i += 1
            print(app_name, modified_name)
    if i > confused_app_num:
        break


# 错误app名写入文件
out_confused_app_names = open(confused_app_names_file, 'w', encoding='utf-8')
for item in confused_app_names:
    out_confused_app_names.write(item)
    out_confused_app_names.write('\n')
out_confused_app_names.close()


# 3 瞎jb写一点模板
templates = [
    '打开{}',
    '开启{}',
    '关闭{}',
    '关掉{}',
    '打开{}吧',
    '开启{}呀',
    '关闭{}哈',
    '关掉{}嘿',
    '我想打开{}这个app',
    '小艾，关了{}烦死了',
    '{}下载完了么',
    '去应用商店搜索{}并安装',
    '后台运行{}十分钟',
    '下载{}',
    '删除{}',
    '删除app{}',
    '小v，我的{}在哪',
    '进{}播放青花瓷',
    '{}卡死了，傻逼',
    '{}好用么',
    '下载{}快点的',
    '小度{}',
    '看看{}，看新闻',
    '我要打开{}看青春有你',
    '使用{}加速',
    '打游戏{}，小v',
    '编不出来了{}',
    '{}科比牛逼',
    '湖人总冠军{}',
    '{}开一下',
    '{}开始下载'
]


# 根据模板生成句子
sentences = []
for item in (app_names + confused_app_names):
    for temp in templates:
        sentences.append(temp.format(item))


# 4 句子写入文件
out_sentences = open(sentences_file, 'w', encoding='utf-8')
for item in sentences:
    out_sentences.write(item)
    out_sentences.write('\n')
out_sentences.close()
