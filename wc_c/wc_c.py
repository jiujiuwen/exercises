#!/usr/bin/env python
#coding=utf8
#Usage: python3 wc_c.py test.txt

import sys
file = sys.argv[1]

def words(str):
    '''
    统计字符串多少字符
    :param str: "sss\n"
    :return: 4
    '''
    n = 0
    for _ in str:
        n += 1
    return n

if __name__ == '__main__':
    byte_count = 0
    with open(file,'r') as f:
        for line in f:
            byte_count += words(line.encode("utf-8")) #py3 ，unicode to str

    print("bytes:%s" % byte_count)


'''
这个我不知道要考啥...总感觉好像和要求不太一样...
utf-8编码后，英文字符1个字节，换行"\n"1个字节，普通汉字3个字节，生僻字4-6个字节。（查的...）
'''