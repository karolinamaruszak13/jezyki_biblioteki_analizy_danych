import unittest
from jezyki_biblioteki_analizy_danych.zad6.quadratic_equation import solve


class QuadraticEquationTest(unittest.TestCase):
    def test_coefficients_value(self):
        self.assertRaises(ValueError, solve, a=0, b=0, c=0)
        self.assertRaises(ValueError, solve, a='t', b=0, c=0)
        self.assertRaises(ValueError, solve, a='t', b='k', c=0)
        self.assertRaises(ValueError, solve, a='t', b='k', c='ghghg')

    def test_if_quadratic(self):
        self.assertRaises(ValueError, solve, a=0, b=0, c=5)
        self.assertEqual(solve(a=0, b=5, c=-10), (2))

    def test_positive_delta(self):
        self.assertEqual(solve(a=1, b=-1, c=0), (0, 1))
        self.assertEqual(solve(a=1, b=1, c=-6), (-3, 2))

    def test_equal_to_zero_delta(self):
        self.assertEqual(solve(a=1, b=2, c=1), (-1))

    def test_negative_delta(self):
        self.assertEqual(solve(a=3, b=0, c=4), ())
        self.assertEqual(solve(a=2, b=0, c=6), ())
        self.assertEqual(solve(a=2, b=-3, c=2), ())
        self.assertEqual(solve(a=-4, b=2, c=-5), ())


if __name__ == '__main__':
    unittest.main()
