"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
输入一个正浮点数值
输出该数值的近似整数值
"""

while True:
    try:
        in_num = input()

        in_num = float(in_num)
        int_part = int(in_num)
        float_part = in_num - int_part

        if float_part < 0.5:
            print(int_part)
        else:
            print(int_part + 1)
    except:
        break