from unittest import TestCase

from source.recursion.power import Power


class TestPower(TestCase):
    def setUp(self):
        self.p = Power(2,4)

    def test_invalid_args_no(self):
        with self.assertRaises(TypeError):
            Power(3)

    def test_invalid_arg_type(self):
        with self.assertRaises(TypeError):
            Power("x",[])
