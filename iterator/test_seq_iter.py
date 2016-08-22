import unittest

from iterator.seqiter import SequenceIterator


class TestSequenceIterator(unittest.TestCase):
    def setUp(self):
        self.empty = SequenceIterator("")
        self.my_list = SequenceIterator([1,2,3,4,5])
        self.my_string = SequenceIterator("abcdefg")

    def test_next_empty(self):
        with self.assertRaises(StopIteration):
            self.assertIsNotNone(next(self.empty))

    def test_next_list_item(self):
        self.assertEqual(next(self.my_list),1)
        self.assertEqual(next(self.my_list),2)

    def test_next_string_char(self):
        self.assertEqual(next(self.my_string),'a')
        self.assertEqual(next(self.my_string),'b')
        self.assertEqual(next(self.my_string),'c')
