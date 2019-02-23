# -*- coding: utf-8 -*-
# 字符串最后一个单词的长度
# 计算字符串最后一个单词的长度，单词以空格隔开。

a = input("input: ")
b = a.split()
print(len(b[-1]))