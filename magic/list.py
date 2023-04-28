import textwrap
from copy import copy


class List:
    __slots__ = ("__list", "__iter_index",
                 "__rever_index", )

    def __init__(self, li):
        """ When an object is instantiated, call it can construct instance object """
        self.__list = li
        self.__iter_index = len(self.__list)
        self.__rever_index = copy(self.__iter_index)

    def __repr__(self):
        """ The official description of the custom object """
        shortened = textwrap.shorten(str(self.__list), 10)
        return f"{self.__class__.__name__}{shortened}"

    def __len__(self):
        """ Support use the built-in function len for this object """
        return len(self.__list)

    def __iter__(self):
        """ Support use the built-in function iter or 'for' statement for this object """
        return self

    def __next__(self):
        """ Implementation logic for specific iterations """
        if self.__iter_index == 0:
            raise StopIteration
        self.__iter_index = self.__iter_index - 1
        return self.__list[self.__iter_index]

    def __reversed__(self):
        """ Support use the built-in function reverse for this object """
        reversed_list = []
        for _ in self.__list:
            reversed_list.append(self.__list[self.__rever_index-1])
            self.__rever_index -= 1
        return reversed_list

    def __getitem__(self, index):
        """ Support use the index for this object """
        return self.__list[index]

    def __setitem__(self, index, item):
        """ Support use the index to set value for this object """
        self.__list[index] = item

    def __delitem__(self, index):
        """ Support use the 'del' to delete value for this object, according to index """
        del self.__list[index]

    def __contains__(self, element):
        """ Support use the built-in operators 'in' for this object """
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
