import unittest

from magic.list import List


class TestList(unittest.TestCase):

    def test_basic(self):
        li = List([1, 2, 3])
        self.assertEqual(li.list, [1, 2, 3])
        self.assertEqual(repr(li), "List[1, 2, 3]")

    def test_list_length(self):
        li = List([1, 2, 3])
        length = len(li)
        self.assertEqual(length, 3)

    def test_iter_and_reversed(self):
        li = List([1, 2, 3])
        new_li = [i for i in li]
        self.assertEqual(new_li, [3, 2, 1])
        reverse_li = reversed(li)
        self.assertEqual(reverse_li, [3, 2, 1])

    def test_getitem(self):
        li = List([1, 2, 3])
        item = li[0]
        self.assertEqual(item, 1)

    def test_delitem(self):
        test_del_li = List([1, 2])
        del test_del_li[0]
        self.assertEqual(test_del_li.list, [2])

    def test_value_in_list(self):
        li = List([1, 2, 3])
        true_result = 1 in li
        self.assertTrue(true_result)
        false_result = -1 in li
        self.assertFalse(false_result)

    def test_list_append(self):
        li = List([1, 2])
        li.append(3)
        self.assertEqual(li.list, [1, 2, 3])

    def test_list_insert(self):
        li = List([1, 2])
        li.insert(2, 3)
        self.assertEqual(li.list, [1, 2, 3])

    def test_list_remove(self):
        li = List([1, 2, 3, 4])
        li.remove(4)
        self.assertEqual(li.list, [1, 2, 3])

    def test_list_pop(self):
        li = List([1, 2, 3, 4])
        li.pop()
        self.assertEqual(li.list, [1, 2, 3])

