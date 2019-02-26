"""
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。
输入一个整数（int类型）
这个数转换成2进制后，输出1的个数
"""
while True:
    try:
        in_num = int(input())

        bin_num = bin(in_num)[2:]
        output = bin_num.count("1")

        print(output)

    except:
        break