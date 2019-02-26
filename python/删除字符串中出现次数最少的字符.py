"""
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。
删除字符串中出现次数最少的字符后的字符串。
"""
while True:
    try:
        str_in = input().lower()
        str_in = list(str_in)

        buf = []
        for i in str_in:
            buf.append([i,str_in.count(i)])
        string = buf
        string.sort()

        min_str = []
        min_count = 0

        while len(min_str) == 0:
            min_count += 1
            for i in range(len(string)):
                if min_count == int(string[i][1]):
                    min_str.append(string[i][0])

        output = []
        for i in range(len(string)):
            if str_in[i][0] not in min_str:
                output.append(str_in[i][0])

        if len(output) > 20:
            output = output[:20]

        print("".join("%s" % id for id in output))
    except:
        break