from unittest import TestCase, mock
from recursion.binary_search import BinarySearch


class TestBinarySearch(TestCase):
    def setUp(self):
        self.sequence = list(range(10))

    def test_search_invalid__no_args(self):
        with self.assertRaises(TypeError):
            bt = BinarySearch()

    def test_search_invalid_args_type(self):
        with self.assertRaises(TypeError):
            bt = BinarySearch('1',2,[1,2])

    def test_search_found(self):
        b = BinarySearch(self.sequence)
        self.assertTrue(b.search(5))

    def test_search_not_found(self):
        b = BinarySearch(self.sequence)
        self.assertFalse(b.search(12))

    def test_recursion_less_than_size_of_sequence(self):
        bs = BinarySearch(self.sequence)
        with mock.patch.object(BinarySearch, 'search', wraps=bs.search) as fake_search:
            bs.search(5)
        self.assertLess(fake_search.call_count,len(self.sequence))



