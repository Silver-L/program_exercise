"""
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

接口说明
/**
 * 反转句子
 *
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);
"""
while True:
    try:
        in_str = input()

        in_split = in_str.split()
        in_split.reverse()

        print(" ".join("%s" % id for id in in_split))
    except:
        break