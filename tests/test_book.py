import os
import unittest

from magic.book import Book, WORDS


BOOK_PATH = os.path.dirname(__file__) + "/book.txt"


class TestBook(unittest.TestCase):

    def test_content(self):
        with Book() as book:
            content = book.get_content()
        self.assertEqual(content, WORDS)

    def tearDown(self):
        if os.path.exists("./book.txt"):
            os.remove(BOOK_PATH)
