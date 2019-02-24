# -*- coding: utf-8 -*-
"""
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
连续输入字符串(输入2次,每个字符串长度小于100)
输出到长度为8的新字符串数组
"""

while True:
    try:
        str_len = 8
        str_list = []
        str_list.append(input())
        str_list.append(input())

        for i in str_list:
            if i.isspace() is True:
                print(i)

            if len(i) < str_len:
                buf = [0 for _ in range(str_len)]
                buf[:len(i)] = i
                print("".join('%s' % id for id in buf))

            if len(i) == str_len:
                print(i)

            if len(i) > str_len:
                if len(i) % str_len == 0:
                    n = len(i) / str_len
                else:
                    n = len(i) / str_len + 1

                for j in range(int(n) - 1):
                    str_out = i[str_len * j: str_len * (j + 1)]
                    print(str_out)

                if len(i[str_len * (int(n) - 1):]) < str_len:
                    buf = [0 for _ in range(str_len)]
                    buf[:len(i[str_len * (int(n) - 1):])] = i[str_len * (int(n) - 1):]
                    print("".join('%s' % id for id in buf))

                else:
                    print(i[str_len * (int(n) - 1):])
    except:
        break