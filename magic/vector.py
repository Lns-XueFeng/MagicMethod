class Vector:
    __slots__ = ("__x", "__y")  # Limit instance variables to _x _y only to save memory

    def __init__(self, x, y):
        """ When an object is instantiated, call it can construct instance object """
        self.__x = x
        self.__y = y

    def __repr__(self):
        """ The official description of the custom object """
        return f"{self.__class__.__name__}({self.__x}, {self.__y})"

    def __str__(self):
        """ The non-official description of the custom object """
        return f"This is a Vector(x: {self.__x}, y: {self.__y})"

    def __add__(self, other):
        """ Support use the built-in operators '+' for between objects """
        return Vector(self.__x + other.x, self.__y + other.y)

    def __sub__(self, other):
        """ Support use the built-in operators '-' for between objects  """
        return Vector(self.__x - other.x, self.__y - other.y)

    def __del__(self):
        """ The del keyword can be used for this object
          and is also called when automatic garbage collection occurs """
        # print(f"{self.__class__.__name__}({self.__x}, {self.__y}) refer -1")
        pass

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
