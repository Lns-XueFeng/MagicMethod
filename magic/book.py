import os


BOOK_PATH = "./book.txt"
WORDS = """Hello Guys!
Python 是一门易于学习、功能强大的编程语言.
它提供了高效的高级数据结构，还能简单有效地面向对象编程.
Python 优雅的语法和动态类型以及解释型语言的本质,
使它成为多数平台上写脚本和快速开发应用的理想语言."""


class Book:
    __slots__ = "__book"

    def __init__(self):
        """ 在对象实例化时, 调用以用于构建实例对象 """
        if not os.path.exists(BOOK_PATH):
            with open(BOOK_PATH, 'w', encoding="utf-8") as fp:
                fp.write(WORDS)
        self.__book = open(BOOK_PATH, 'r', encoding="utf-8")

    def __repr__(self):
        """ 自定义对象的官方描述 """
        return f"{self.__class__.__name__}"

    def __enter__(self):
        """ 在with语句结束之前做些什么 """
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        """ 在with语句结束的时候做些什么 """
        self.__book.close()

    def get_content(self):
        return self.__book.read()


if __name__ == "__main__":
    book = Book()
    print(book)
    with book as b:
        content = book.get_content()
        print(content)
