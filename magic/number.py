class Number:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.num}"

    def __abs__(self):
        return abs(self.num)

    def __neg__(self):
        return -self.num


class IntNumber(Number):
    pass


class FloatNumber(Number):
    pass
