"""
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
先输入键值对的个数
然后输入成对的index和value值，以空格隔开
输出合并后的键值对（多行）
"""
while True:
    try:
        in_key = input()
        in_num = []
        for i in range(int(in_key)):
            in_num.append(input().split())

        index = []

        for i in range(int(in_key)):
            if in_num[i][0] not in index:
                index.append(in_num[i][0])

        index = list(map(int, index))
        index.sort()

        value = []
        for i in index:
            buf = 0
            for j in range(int(in_key)):
                if i == int(in_num[j][0]):
                    buf += int(in_num[j][1])
            value.append(buf)

        for i in range(len(index)):
            print("%d %d" % (index[i], value[i]))
    except:
        break
