#!/usr/bin/env python
#coding=utf8
def char_ord(s):
    h1 = ord(s) #转换为ASCII 十进制值，小写字母值唯一
    return h1

def get_total(str): #字符串所有ASCII值总和
    result = 0
    for c in str:
        result += char_ord(c)
    return result

if __name__=="__main__":
    str_1 = raw_input("string_1:")
    str_2 = raw_input("string_2:")
    if get_total(str_1) == get_total(str_2):
        print True
    else:
        print False


'''
觉得这样判断好像都是可以判断的，还挺方便的。这样会有什么问题嘛 0 0？
'''