class Book:
    def __init__(self):
        self.book = open("book.txt", 'r', encoding="utf-8")

    def get_content(self):
        return self.book.read()

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.book.close()


if __name__ == "__main__":
    book = Book()
    with book as b:
        content = book.get_content()
        print(content)
