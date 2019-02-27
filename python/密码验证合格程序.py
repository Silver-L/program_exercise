"""
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有相同长度超2的子串重复
说明:长度超过2的子串
??????

"""
import re
try:
    while 1:
        s = input()
        a = re.findall(r'(.{3,}).*\1', s)
        b1 = re.findall(r'\d', s)
        b2 = re.findall(r'[A-Z]', s)
        b3 = re.findall(r'[a-z]', s)
        b4 = re.findall(r'[^0-9A-Za-z]', s)
        print ('OK') if ([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(s) > 8) else ('NG')

except:
    pass

# while True:
#     try:
#         str_in = input()
#
#         output = "OK"
#         # check rule 1
#         if (len(str_in) <= 8):
#             output = "NG"
#
#         # check rule 2
#         if (str_in.isdigit() == True or str_in.isalpha() == True):
#             output = "NG"
#
#         str_list = list(str_in)
#         no_code = []
#         no_dig = []
#         for i in str_list:
#             if i.isalnum() != False:
#                 no_code.append(i)
#
#         for i in no_code:
#             if i.isdigit() == False:
#                 no_dig.append(i)
#
#         no_dig = "".join(no_dig)
#
#         if len(no_dig) == 0:
#             output = "NG"
#
#         if (no_dig.lower() == no_dig and no_dig.upper() == no_dig):
#             output = "NG"
#
#         # check rule 3
#         error = 0
#         for i in range(3, len(str_in)-3):
#             count = 0
#             for j in range(0, len(str_in)):
#                 if (i+j)>len(str_in):
#                     break
#
#                 buf = str_in[count:i + j]
#                 count += 1
#
#                 buf_string = str_in
#                 buf_string = buf_string.replace(buf, "")
#                 if len(buf_string) != len(str_in) - len(buf):
#                     error += 1
#
#                 if error > 0:
#                     output = "NG"
#
#         print(output)
#
#     except:
#         break
