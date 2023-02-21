import unittest

from magic.vector import Vector


class TestVector(unittest.TestCase):

    def test_basic(self):
        a = Vector(2, 3)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(repr(a), "Vector(2, 3)")
        self.assertEqual(str(a), "This is a Vector(x: 2, y: 3)")

    def test_operate(self):
        a, b = Vector(2, 3), Vector(2, 3)
        self.assertEqual(repr(a + b), "Vector(4, 6)")
        self.assertEqual(repr(a - b), "Vector(0, 0)")
