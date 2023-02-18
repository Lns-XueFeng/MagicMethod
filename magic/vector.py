class Vector:
    def __init__(self, x, y):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        __slots__ = ("_x", "_y")   # 限制实例变量仅为_x, _y, 以节省内存
        self._x = x
        self._y = y

    def __repr__(self):
        """ 自定义对象的官方描述 """
        return f"{self.__class__.__name__}({self._x}, {self._y})"

    def __str__(self):
        """ 自定义对象的非官方描述 """
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
