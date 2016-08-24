from unittest import TestCase, mock
from recursion.english_ruler import EnglihRuler


class TestEnglishRuler(TestCase):

    def test_parameters_count(self):
        with self.assertRaises(TypeError):
            r = EnglihRuler("hey few args")
            r.run()

    def test_parameters_types(self):
        with self.assertRaises(TypeError):
            r = EnglihRuler("hey few args", 11)
            r.run()

    def test_recurtion_n_times(self):
        r = EnglihRuler(1,3)
        with mock.patch.object(EnglihRuler, 'draw_interval', wraps=r.draw_interval) as fake_draw_interval:
            r.run()
        self.assertEqual(fake_draw_interval.call_count,7)