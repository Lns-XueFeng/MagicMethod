import textwrap
from copy import copy


class List:
    def __init__(self, *args):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        self.list = [*args]
        self.iter_index = len(self.list)
        self.rever_index = copy(self.iter_index)

    def __repr__(self):
        """ 自定义对象的官方描述 """
        shortened = textwrap.shorten(str(self.list), 10)
        return f"{self.__class__.__name__}{shortened}"

    def __len__(self):
        """ 可对该对象使用内置函数len """
        return len(self.list)

    def __iter__(self):
        """ 可让该对象为可迭代对象 """
        return self

    def __next__(self):
        """ 具体迭代的实现逻辑 """
        if self.iter_index == 0:
            raise StopIteration
        self.index = self.iter_index - 1
        return self.list[self.index]

    def __reversed__(self):
        """ 可对该对象使用内置函数reverse """
        reversed_list = []
        for _ in self.list:
            reversed_list.append(self.list[self.rever_index-1])
            self.rever_index -= 1
        return reversed_list

    def __getitem__(self, index):
        """ 可对该对象使用索引去值 """
        return self.list[index]

    def __delitem__(self, element):
        """ 可根据索引对该对象值进行删除 """
        self.list.remove(element)

    def __contains__(self, element):
        """ 可对该对象使用内置操作符in """
        return element in self.list

    def append(self, element):
        pass

    def insert(self, index, element):
        pass

    def remove(self, element):
        pass

    def pop(self):
        pass


if __name__ == "__main__":
    l = List(1, 2, 3, 4, 4)
    print(l)
    print(reversed(l))
    print(l[1])
    print(1 in l)
