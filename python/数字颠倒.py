"""
输入一个整数，将这个整数以字符串的形式逆序输出
程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001
"""

while True:
    try:
        input_str = input()

        input_str = list(input_str)
        input_str.reverse()

        print("".join("%s" % id for id in input_str))

    except:
        break