"""
写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。例如：
输入N个字符
输出该字符串反转后的字符串
"""
while True:
    try:
        in_str = input()

        in_str = list(in_str)
        in_str.reverse()

        print("".join("%s" % id for id in in_str))
    except:
        break