#!/usr/bin/env python
#coding=utf8
import sys
file = sys.argv[1]

def word_split(s):
    if s in ".,!?;:\"(){}[]" or s.isspace(): #空格和标点符号
        return True

def is_letter(word):
    try:
        if word.isalpha() or word in "'":  # 整数没有isalpha类型
            return True
    except Exception as e:
        return False

def get_len(_list):
    n = 0
    for _ in _list:
        n += 1
    return n

def split_reserse(index):
    if index:
        index == False
    else:
        index == True
    return index

def split_string(str):
    out_list = []
    temp_list = []

    split_index = True
    for i in context:
        if word_split(i):
            split_index = split_reserse(split_index)
            out_list.append(temp_list)
            temp_list = []
        else: #非分隔符
            temp_list.append(i)
    return out_list

def all_letter(_list):
    for i in xrange(get_len(_list)):
        if not is_letter(_list[i]):
            return False
    return _list

if __name__ == '__main__':
    w_count = 0 #counter
    with open(file, 'r') as f:
        context = f.read()

        for word_list in split_string(context):
            #print word_list  #这里打印所有temp_list，两分隔符之间的所有元素
            if all_letter(word_list):
                w_count += 1
                print ''.join(word_list),  #打印的是所有单词

    print w_count

'''
test.txt:pd $$ d%s  $$d s #$d%% d%  8  ttts  $$$      r     #$% sa.
1、分隔符分割字符串，split_index 为布尔值 ，每次遇分隔符反转
['p', 'd']
['$', '$']
['d', '%', 's']
[]   #分隔符符号也会记入temp_list
['$', '$', 'd']
['s']
['#', '$', 'd', '%', '%']
...
2、判断这些list里面如果全是字母，则计数器加1
3、与wc -w区别
wc命令：
     -w      The number of words in each input file is written to the standard output.
wc -w命令，把数字以及乱码字符也会当做一个word。
这个脚本仅把两分隔符之间纯字母当做一个word。
所以运算结果的number会 <= wc -w
wc_w_test.txt内容(单行)：count the words  #$%^&   780    hahaha
~/exercise/words_count(master*) » wc -w wc_w_test.txt
       6 wc_w_test.txt
~/exercise/words_count(master*) » python split_count.py wc_w_test.txt
count the words hahaha 4
这里脚本运行只有4个单词，wc -w运行有6个单词
-------
没有去设计复杂的链表结构了，虽然这个方法有点浪费。。
'''