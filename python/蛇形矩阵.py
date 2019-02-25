"""
题目说明
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
样例输入
5
样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
接口说明
原型
void GetResult(int Num, char * pResult);
输入参数：
        int Num：输入的正整数N
输出参数：
        int * pResult：指向存放蛇形矩阵的字符串指针
        指针指向的内存区域保证有效
返回值：
        void
"""
while True:
    try:
        in_num = input()

        output = []
        output_first = []
        for i in range(int(in_num)):
            if i == 0 :
                output_first.append(1)
            else:
                output_first.append(output_first[i-1] + i)
            for j in range(int(in_num) - i):

                if j == 0:
                    output.append(output_first[i])
                else:
                    output.append(output[j-1] + j + i + 1 )
            print(" ".join("%s" % id for id in output ))
            output = []
    except:
        break
