#!/usr/bin/env python
#coding=utf8
#count every letter appear times,at last,compare list

class str_to_dict:
    def __init__(self,in_str):
        self.in_str = in_str

    def word_keys(self):
        '''
        input:abcc
        :return: ['a', 'b', 'c']
        '''
        key_list = []
        for i in self.in_str:
            if i not in key_list: #no repeat key
                key_list.append(str(i))
        return  key_list

    def letter_times(self,c):
        n = 0
        for i in self.in_str:
            if i == c :
                n += 1
        return (c,n)

    def word_count(self):
        '''
        input:abcc
        :return: [('a', 1), ('b', 1), ('c', 2)]
        '''
        ret_list = []
        for c in self.word_keys():
            ret_list.append(self.letter_times(c))
        return ret_list

if __name__ == "__main__":
    str_1 = raw_input("string_1:")
    str_2 = raw_input("string_2:")

    one = str_to_dict(str_1)
    two = str_to_dict(str_2)

    if [val for val in one.word_keys() if val not in two.word_keys()] == []: #key一样
        if [val for val in one.word_count() if val not in two.word_count()] == []: #key出现的次数一样
            print True
            exit()
    print False

'''
用了list和tuple数据结构实现了类似字典的类，然后比较两个列表。
'''
