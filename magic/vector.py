class Vector:
    __slots__ = ("__x", "__y")  # 限制实例变量仅为_x, _y, 以节省内存

    def __init__(self, x, y):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        self.__x = x
        self.__y = y

    def __repr__(self):
        """ 自定义对象的官方描述 """
        return f"{self.__class__.__name__}({self.__x}, {self.__y})"

    def __str__(self):
        """ 自定义对象的非官方描述 """
        return f"This is a Vector(x: {self.__x}, y: {self.__y})"

    def __add__(self, other):
        """ 可在该对象之间使用内置操作符+ """
        return Vector(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other):
        """ 可在该对象之间使用内置操作符- """
        return Vector(self.__x - other.x, self.__y - other.y)

    def __del__(self):
        """ 可对该对象使用del关键字 当自动垃圾回收时亦会调用 """
        # print(f"{self.__class__.__name__}({self.__x}, {self.__y}) refer -1")
        pass

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
