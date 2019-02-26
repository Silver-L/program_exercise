"""
功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
最后一个数后面也要有空格
详细描述：
函数接口说明：
public String getResult(long ulDataInput)
输入参数：
long ulDataInput：输入的正整数
返回值：
String
输入一个long型整数

按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

"""
while True:
    try:
        in_num = int(input())

        i = 2
        prime = []

        while in_num != 1:
            if in_num%i == 0:
                in_num /= i
                prime.append(i)

            else:
                i += 1

        prime.append("")
        print(" ".join("%s" % id for id in prime))

    except:
        break

