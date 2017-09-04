#!/usr/bin/env python
#coding=utf8

def word_split(s):
    if s in ".,! ": #空格和标点符号
        return True

#判断全为字母的类，下一个字母为分隔符，停止
class Word: #单个字母判断
	def __init__(self,word,word_next=None):
		self.word = word
		self.next = word_next

class WordList: #生成大链表
    def __init__(self):
        self._head = None
        self._rear = None

    def is_letter(self,word):
        try:
            if word.isalpha(): #整数没有isalpha类型
                return True
        except Exception as e:
            return False
        # return word.isalpha() is True

    def add(self,data):
        #p = Word(data)
        if self._head is None: #第一个元素
            self._head = Word(data)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = Word(data)

    def print_all(self):
        p = self._head
        while True:
            print(p.word)
            p = p.next
            if p is self._rear:
                break

    def judge(self): #判断是否纯字母
        p = self._head
        while True:
            if not self.is_letter(p.word):
                return False
            else:
                p = p.next
                if p is self._rear:
                    break
        return True

    def split_word(self):
        count = 0
        p = self._head
        while True:
            print(p.word)
            p = p.next
            if word_split(p.word): #下一个字符
                count += 1
            if p.next is self._rear:
                break
        return count

w = WordList()
# w.add("w")
# w.add(",")
# w.add("9")
# w.add(" ")
# w.add("a")
# w.add("l")
# w.add(".")
# w.add("s")
# print w.split_word()
#print w.judge()

t_str = "pd $$ d%s  $$d s #$d%% d%  8    $$$      r     #$% sa."#2
for i in t_str:
    if word_split(i):
        break
    else:
        w.add(i)

# print w.split_word()


# s = "have a good day." #5
#
# n = 0
# for i in s:
#     if word_split(i):
#         n += 1
#     else:
#         pass
# print n




