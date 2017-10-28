#!/usr/bin/env python
# coding=utf-8
class Mapping(object):
    def __init__(self, key, value, data=None):
        self.key = key
        self.value = value
        self.data = (self.key, self.value)


class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.data = Mapping(key, value)
        self.left = left
        self.right = right


class BinTree(object):
    def __init__(self):
        self._root = None  # self._root.data.data = tuple
        self.all_datas = []

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            entry_key = bt.data.key  # key
            if key < entry_key:
                bt = bt.left
            elif key > entry_key:
                bt = bt.right
            else:
                return bt.data.value  # value ,[(key, value)]
        raise KeyError(key)

    def insert(self, key, value):
        bt = self._root
        if not bt:  # null
            self._root = Node(key, value)
            return
        while True:
            entry_key = bt.data.key
            if key < entry_key:
                if bt.left is None:
                    bt.left = Node(key, value)
                    return
                else:
                    bt = bt.left
            elif key > entry_key:
                if bt.right is None:
                    bt.right = Node(key, value)
                    return
                else:
                    bt = bt.right
            else:
                bt.data = Node(key, value).data  # overwrite
                return

    def delete(self, key):
        p, q = None, self._root
        if not q:
            raise KeyError("NULL node: %" % str(key))  # null tree

        while q and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            elif key > q.data.key:
                q = q.right

            if not q:
                raise KeyError("key %s NOT EXIST" % str(key))
            #print(q.data.data, p.data.data)

        if not q.left:  # no left
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        r = q.left  # have left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def _printall(self, root):
        if root is None:
            return

        if root.data.data not in self.all_datas:  # repeat add
            self.all_datas.append(root.data.data)

        self._printall(root.left)
        self._printall(root.right)

    def printall(self, root):
        self.all_datas = []  # clear list, for delete
        self._printall(root)
        return self.all_datas


class MyDict(object):
    def __init__(self):
        self.dict_tree = BinTree()

    def get(self, key_in):
        return self.dict_tree.search(key_in)

    def delete(self, key):
        self.dict_tree.delete(key)

    def values(self):
        temp_values = []
        for key, value in self.dict_tree.printall(self.dict_tree._root):
            temp_values.append(value)
        return temp_values

    def keys(self):
        temp_keys = []
        for key, value in self.dict_tree.printall(self.dict_tree._root):
            temp_keys.append(key)
        return temp_keys

    def items(self):
        return self.dict_tree.printall(self.dict_tree._root)

    def set(self, key, value):
        self.dict_tree.insert(key, value)


md = MyDict()
md.set("one", 1)
md.set("two", 3)
md.set("three", 300)
md.set("three", 4)
md.set("four", 100)

#md.delete("four")

print md.items()

#print md.keys()
# print md.keys()
# print md.values()

md.delete("two")
md.delete("oo")

print md.items()

# print md.get("two")

#          one
#        /     \
#    four       two
#              /
#           three
