import math
from unittest import TestCase, mock
from source.recursion.power import Power


class TestPower(TestCase):
    def setUp(self):
        self.p = Power(2,2)

    def test_invalid_args_no(self):
        with self.assertRaises(TypeError):
            Power(3)

    def test_invalid_arg_type(self):
        with self.assertRaises(TypeError):
            Power("x",[])

    def test_square(self):
        result = self.p.calculate_power()
        self.assertEqual(4, result)

    def test_cube(self):
        result = self.p.calculate_power(3)
        self.assertEqual(8, result)

    def test_power_n(self):
        for j in range(5):
            self.assertEqual(self.p.calculate_power(j),math.pow(2,j))

    def test_recursion_less_than_power(self):
        p = Power(2,1)
        with mock.patch.object(Power, 'calculate_power', wraps=p.calculate_power) as fake_calculate_power:
            p.calculate_power(5)
        self.assertLess(fake_calculate_power.call_count,5)
