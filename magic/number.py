class Number:
    __slots__ = "num"

    def __init__(self, num):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        self.num = num

    def __repr__(self):
        """ 自定义对象的官方描述 """
        return f"{self.__class__.__name__}: {self.num}"

    def __abs__(self):
        """ 可对该对象使用内建函数abs """
        return abs(self.num)

    def __neg__(self):
        """ 可对该对象使用内置操作符- """
        return -self.num

    def __add__(self, other):
        """ 可对该对象之间使用内置运算符+ """
        return self.__class__(self.num + other.num)

    def __sub__(self, other):
        """ 可对该对象之间使用内置运算符- """
        return self.__class__(self.num - other.num)

    def __mul__(self, other):
        """ 可对该对象之间使用内置运算符* """
        return self.__class__(self.num * other.num)

    def __truediv__(self, other):
        """ 可对该对象之间使用内置运算符/ """
        return self.__class__(self.num / other.num)

    def __mod__(self, other):
        """ 可对该对象之间使用内置运算符% """
        return self.__class__(self.num % other.num)

    def __gt__(self, other):
        """ 可对该对象之间使用内置运算符> """
        return self.num > other.num

    def __ge__(self, other):
        """ 可对该对象之间使用内置运算符>= """
        return self.num >= other.num

    def __lt__(self, other):
        """ 可对该对象之间使用内置运算符< """
        return self.num < other.num

    def __le__(self, other):
        """ 可对该对象之间使用内置运算符<= """
        return self.num <= other.num

    def __eq__(self, other):
        """ 可对该对象之间使用内置运算符== """
        return self.num == other.num

    def __ne__(self, other):
        """ 可对该对象之间使用内置运算符!= """
        return self.num != other.num

    def __bool__(self):
        """ 自定义该对象的bool判断 """
        if self.num > 0:
            return True
        return False


class IntNumber(Number):
    __int_num = None

    def __new__(cls, num):
        """
        在对象实例化(__init__调用之前) => 在class建立对象这个时间段
        被调用，以用于定制化对象，这里是在构建实例对象之前检查num的类型是否为int
        """
        if not isinstance(num, int):
            cls.__int_num = int(num)
        return super().__new__(cls)

    def __init__(self, num):
        super().__init__(self)
        self.num = self.__int_num

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.num}"


class FloatNumber(Number):
    __float_num = None

    def __new__(cls, num):
        """
        在对象实例化(__init__调用之前) => 在class建立对象这个时间段
        被调用，以用于定制化对象，这里是在构建实例对象之前检查num的类型是否为float
        """
        if not isinstance(num, float):
            cls.__float_num = float(num)
        return super().__new__(cls)

    def __init__(self, num):
        super().__init__(self)
        self.num = self.__float_num

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.num}"
