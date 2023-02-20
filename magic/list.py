import textwrap
from copy import copy


class List:
    __slots__ = ("__list", "__iter_index",
                 "__rever_index", "__list_index", )

    def __init__(self, *args):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        self.__list = [*args]
        self.__iter_index = len(self.__list)
        self.__rever_index = copy(self.__iter_index)
        self.__list_index = None

    def __repr__(self):
        """ 自定义对象的官方描述 """
        shortened = textwrap.shorten(str(self.__list), 10)
        return f"{self.__class__.__name__}{shortened}"

    def __len__(self):
        """ 可对该对象使用内置函数len """
        return len(self.__list)

    def __iter__(self):
        """ 可让该对象为可迭代对象 """
        return self

    def __next__(self):
        """ 具体迭代的实现逻辑 """
        if self.__iter_index == 0:
            raise StopIteration
        self.__list_index = self.__iter_index - 1
        return self.__list[self.__list_index]

    def __reversed__(self):
        """ 可对该对象使用内置函数reverse """
        reversed_list = []
        for _ in self.__list:
            reversed_list.append(self.__list[self.__rever_index-1])
            self.__rever_index -= 1
        return reversed_list

    def __getitem__(self, index):
        """ 可对该对象使用索引去值 """
        return self.__list[index]

    def __delitem__(self, element):
        """ 可根据索引对该对象值进行删除 """
        self.__list.remove(element)

    def __contains__(self, element):
        """ 可对该对象使用内置操作符in """
        return element in self.__list

    @property
    def list(self):
        return self.__list

    def append(self, element):
        self.__list.append(element)

    def insert(self, index, element):
        self.__list.insert(index, element)

    def remove(self, element):
        self.__list.remove(element)

    def pop(self):
        self.__list.pop()
