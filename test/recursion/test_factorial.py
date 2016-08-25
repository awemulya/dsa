from unittest import TestCase

from recursion.factorial import Factorial


class TestFactorial(TestCase):
    def setUp(self):
        self.n = 10
        self.m = 9
        self.one = 0

    def test_factorial_of_zero(self):
        self.assertEqual(Factorial.factorial(self.one),1)

    def test_factorial(self):
        self.assertEqual(Factorial.factorial(self.n),10*9*8*7*6*5*4*3*2*1)

    def test_factorial_n_and_one_less_n(self):
        self.assertEqual(Factorial.factorial(self.n),self.n * Factorial.factorial(self.m))
