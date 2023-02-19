import unittest

from magic.decorator import show_name


class TestDecorator(unittest.TestCase):

    def test_wrapped_name(self):
        name = show_name()
        self.assertEqual(name, "Lns-XueFeng")
