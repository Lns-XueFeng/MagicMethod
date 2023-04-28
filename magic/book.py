import os


BOOK_PATH = "./book.txt"
WORDS = """ Hello Guys!
Python is a beautiful language, has a powerful ability,
it gives a effective advance structure and can face-to-object program """


class Book:
    __slots__ = "__book"

    def __init__(self):
        """ When an object is instantiated, call it can construct instance object """
        if not os.path.exists(BOOK_PATH):
            with open(BOOK_PATH, 'w', encoding="utf-8") as fp:
                fp.write(WORDS)
        self.__book = open(BOOK_PATH, 'r', encoding="utf-8")

    def __repr__(self):
        """ The official description of the custom object """
        return f"{self.__class__.__name__}"

    def __enter__(self):
        """ To do something before 'with' statement end """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ To do something after 'with' statement end """
        self.__book.close()

    def get_content(self):
        return self.__book.read()


if __name__ == "__main__":
    with Book() as book:
        content = book.get_content()
        print(content)
