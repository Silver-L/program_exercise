"""
写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
输入一个十六进制的数值字符串。
输出该数值的十进制字符串。
"""
while True:
    try:
        hex_in = input()
        output = ("".join("%s" % id for id in hex_in))
        print(int(output, 16))
    except:
        break