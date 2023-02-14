class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"{self.__class__.__name__}({self._x}, {self._y})"

    def __str__(self):
        return f"This is a Vector(x：{self._x}, y：{self._y})"

    def __add__(self, other):
        return Vector(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        return Vector(self._x - other.x, self._y - other.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __del__(self):
        print(f"{self.__class__.__name__}({self._x}, {self._y}) has freed")


if __name__ == "__main__":
    a = Vector(2, 3)
    print(repr(a))   # == >>>a
    print(str(a))   # == print(a)

    b = Vector(3, 4)
    c = a + b
    print(repr(c))   # Vector(5, 7)
    d = a - b
    print(repr(d))   # Vector(-1, -1)



