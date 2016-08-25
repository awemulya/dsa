import unittest

from vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector = Vector(3)

    def test_len(self):
        self.assertEqual(len(self.vector),3)

    def test_vector_str(self):
        self.assertIsInstance(str(self.vector),str)

    def test_get_attr(self):
        self.assertEqual(self.vector[1],0)

    def test_out_of_index(self):
        with self.assertRaises(IndexError):
            self.vector[3]

    def test_set_attr(self):
        self.vector[1] = 2
        self.assertEqual(self.vector[1],2)

    def test_addition(self):
        self.vector1 = Vector(3)
        self.vector + self.vector1

    def test_different_length_fails(self):
        self.vector1 = Vector(5)
        with self.assertRaises(ValueError):
            self.vector1 + self.vector

    def test_substraction(self):
        self.vector1 = Vector(3)
        self.vector - self.vector1

    def test_equal(self):
        self.vector1 = Vector(3)
        self.assertTrue(self.vector1 == self.vector)

    def test_not_equal(self):
        self.vector1 = Vector(3)
        self.vector1[1] = 1
        self.assertTrue(self.vector1 != self.vector)


if __name__ == '__main__':
    unittest.main()