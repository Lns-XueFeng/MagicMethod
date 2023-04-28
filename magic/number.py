class Number:
    __slots__ = "num"

    def __init__(self, num):
        """ When an object is instantiated, call it can construct instance object """
        self.num = num

    def __repr__(self):
        """ The official description of the custom object """
        return f"{self.__class__.__name__}: {self.num}"

    def __abs__(self):
        """ Support use the built-in function abs for this object """
        return abs(self.num)

    def __neg__(self):
        """ Support use the built-in operators '-' for this object """
        return -self.num

    def __add__(self, other):
        """ Support use the built-in operators '+' for between objects """
        return self.__class__(self.num + other.num)

    def __sub__(self, other):
        """ Support use the built-in operators '-' for between objects """
        return self.__class__(self.num - other.num)

    def __mul__(self, other):
        """ Support use the built-in operators '*' for between objects """
        return self.__class__(self.num * other.num)

    def __truediv__(self, other):
        """ Support use the built-in operators '/' for between objects """
        return self.__class__(self.num / other.num)

    def __mod__(self, other):
        """ Support use the built-in operators '%' for between objects """
        return self.__class__(self.num % other.num)

    def __gt__(self, other):
        """ Support use the built-in operators '>' for between objects """
        return self.num > other.num

    def __ge__(self, other):
        """ Support use the built-in operators '>=' for between objects """
        return self.num >= other.num

    def __lt__(self, other):
        """ Support use the built-in operators '<' for between objects """
        return self.num < other.num

    def __le__(self, other):
        """ Support use the built-in operators '<=' for between objects """
        return self.num <= other.num

    def __eq__(self, other):
        """ Support use the built-in operators '==' for between objects """
        return self.num == other.num

    def __ne__(self, other):
        """ Support use the built-in operators '!=' for between objects """
        return self.num != other.num

    def __bool__(self):
        """ Support use the built-in function bool for this object """
        if self.num > 0:
            return True
        return False


class IntNumber(Number):
    __int_num = None

    def __new__(cls, num):
        """
        Before object instantiation (before __init__ call)
        => is called during the time period during which the object is created in class
        """
        if not isinstance(num, int):
            cls.__int_num = int(num)
        else:
            cls.__int_num = num
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
        Before object instantiation (before __init__ call)
        => is called during the time period during which the object is created in class
        """
        if not isinstance(num, float):
            cls.__float_num = float(num)
        else:
            cls.__float_num = num
        return super().__new__(cls)

    def __init__(self, num):
        super().__init__(self)
        self.num = self.__float_num

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.num}"
