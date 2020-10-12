import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):
    """
    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)
    """

    def test_basic(self):
        t = OrderedList()
        self.assertTrue(t.is_empty())
        t.add(1)
        self.assertFalse(t.is_empty())

    def test_add(self):
        t = OrderedList()
        self.assertTrue(t.add(1))
        self.assertFalse(t.add(1))
        t.add(2)
        self.assertEqual(t.pop(1), 2)
        self.assertTrue(t.add(0.5))


    def test_add_ascending(self):
        t = OrderedList()
        self.assertTrue(t.add(3))
        self.assertTrue(t.add(6))
        self.assertTrue(t.add(7))
        self.assertTrue(t.add(2))
        self.assertEqual(t.dummy.next.item, 2)
        self.assertEqual(t.dummy.prev.item, 7)

    def test_some_more(self):
        t = OrderedList()
        self.assertTrue(t.add(5))
        self.assertTrue(t.add(7))
        self.assertTrue(t.add(6))

    def test_remove(self):
        t = OrderedList()
        self.assertFalse(t.remove(5))
        self.assertTrue(t.add(5))
        self.assertTrue(t.add(7))
        self.assertTrue(t.add(6))
        self.assertTrue(t.remove(6))
        self.assertFalse(t.remove(54))


    def test_index(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        self.assertEqual(t.index(1), 0)
        self.assertIsNone(t.index(6))
        self.assertEqual(t.index(2), 1)


    def test_pop_size_ind_error(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        with self.assertRaises(IndexError):
            t.pop(3)


    def test_pop_neg_ind_error(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        with self.assertRaises(IndexError):
            t.pop(-1)


    def test_pop(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        self.assertEqual(1, t.pop(0))

    def test_python_list(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        self.assertEqual([1, 2], t.python_list())

    def test_search(self):
        l = OrderedList()
        l.add(5)
        l.add(19)
        l.add(12)
        l.add(7)
        l.add(22)
        l.add(3)
        self.assertTrue(l.search(5))
        self.assertFalse(l.search(4))

    def test_size(self):
        l = OrderedList()
        l.add(5)
        l.add(19)
        l.add(12)
        self.assertEqual(3, l.size())

    def test_reverse(self):
        t = OrderedList()
        t.add(1)
        t.add(2)
        self.assertEqual([2, 1], t.python_list_reversed())



if __name__ == '__main__':
    unittest.main()
