from unittest import TestCase
from source.recursion.linear_sum import LinearSum, BinarySum


class TestLinearSum(TestCase):
    def setUp(self):
        self.s = list(range(10))
        self.sum_total = LinearSum.sum(self.s, len(self.s))

    def test_sum_total(self):
        self.assertEqual(self.sum_total,sum(self.s))

    def test_sum_fragments(self):
        self.assertEqual(sum(self.s[:5]),LinearSum.sum(self.s,5))


class TestBinarySum(TestCase):
    def setUp(self):
        self.s = list(range(10))

    def test_sum_total(self):
        self.assertEqual(sum(self.s),BinarySum.sum(self.s))



