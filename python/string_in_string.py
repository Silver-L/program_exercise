# -*- coding: utf-8 -*-
# 写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
# 输入一个有字母和数字以及空格组成的字符串，和一个字符。

str_1 = input().lower()
str_2 = input().lower()
str_1_split = list(str_1)

num = 0
for i in str_1_split:
    result = str_2 in i
    if result is True:
        num += 1
print(num)
