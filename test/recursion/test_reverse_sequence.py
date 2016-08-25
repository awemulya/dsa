from unittest import TestCase
from source.recursion.reverse_sequence import ReverseSeq
class TestReverseSeq(TestCase):

    def setUp(self):
        self.seq = list(range(10))

    def test_reverse(self):
        list_copy = self.seq.copy()
        self.assertEqual(ReverseSeq.reverse(list_copy),self.seq[::-1])

    def test_reverse_good(self):
        copy = list(range(10))
        ReverseSeq.good_reverse(copy, 0, len(copy))
        self.assertEqual(copy, self.seq[::-1])