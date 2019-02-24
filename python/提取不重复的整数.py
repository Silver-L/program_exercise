"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
输入一个int型整数
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
"""
while True:
    try:
        in_num = input()
        out_num = []

        in_num = list(in_num)
        in_num.reverse()

        for i in in_num:
            if i not in out_num:
                out_num.append(i)

        print("".join('%s' % id for id in out_num))

    except:
        break