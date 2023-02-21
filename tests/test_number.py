import unittest

from magic.number import IntNumber, FloatNumber


class TestIntNumber(unittest.TestCase):

    def test_basic(self):
        int_number = IntNumber(10)
        self.assertEqual(repr(int_number), "IntNumber: 10")
        self.assertEqual(int_number.num, 10)
        self.assertEqual(abs(int_number), 10)

    def test_operate(self):
        a, b = IntNumber(1), IntNumber(1)
        self.assertEqual(-a, -1)
        self.assertEqual((a + b).num, 2)
        self.assertEqual((a - b).num, 0)
        self.assertEqual((a * b).num, 1)
        self.assertEqual((a / b).num, 1)
        self.assertEqual((a % b).num, 0)

    def test_relative(self):
        a, b = IntNumber(1), IntNumber(2)
        self.assertFalse(a > b)
        self.assertTrue(a < b)
        self.assertFalse(a >= b)
        self.assertTrue(a <= b)
        self.assertTrue(a != b)
        self.assertTrue(bool(a))


class TestFloatNumber(unittest.TestCase):

    def test_basic(self):
        float_number = FloatNumber(10.1)
        self.assertEqual(repr(float_number), "FloatNumber: 10.1")
        self.assertEqual(float_number.num, 10.1)
        self.assertEqual(abs(float_number), 10.1)

    def test_operate(self):
        c, d = FloatNumber(1.1), FloatNumber(1.1)
        self.assertEqual(-c, -1.1)
        self.assertEqual((c + d).num, 2.2)
        self.assertEqual((c - d).num, 0.0)
        self.assertEqual((c * d).num, 1.2100000000000002)
        self.assertEqual((c / d).num, 1.0)
        self.assertEqual((c % d).num, 0)

    def test_relative(self):
        c, d = FloatNumber(1), FloatNumber(2)
        self.assertFalse(c > d)
        self.assertTrue(c < d)
        self.assertFalse(c >= d)
        self.assertTrue(c <= d)
        self.assertTrue(c != d)
        self.assertTrue(bool(c))
