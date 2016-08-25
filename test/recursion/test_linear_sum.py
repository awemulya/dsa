from unittest import TestCase
from recursion.linear_sum import LinearSum


class LinearSumTest(TestCase):
    def setUp(self):
        self.s = list(range(10))
        self.sum_total = LinearSum.sum(self.s, len(self.s))

    def test_sum_total(self):
        self.assertEqual(self.sum_total,sum(self.s))

    def test_sum_fragments(self):
        self.assertEqual(sum(self.s[:5]),LinearSum.sum(self.s,5))


