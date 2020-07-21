from simple_calc import SimpleCalc
import unittest


class Calctests(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 2), 4)
        self.assertEqual(self.calc.add(-5, -2), -7)
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertIsNotNone(self.calc.add(0, 0))

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)
        self.assertEqual(self.calc.subtract(-7, 3), -10)
        self.assertEqual(self.calc.subtract(-10, -2), -8)
        self.assertEqual(self.calc.subtract(4, -2), 6)
        self.assertIsNotNone(self.calc.subtract(0, 0))

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 0), 0)
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(3, -2), -6)
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertIsNotNone(self.calc.multiply(0, 0))

    def test_divide(self):
        self.assertEqual(self.calc.divide(100, 10), 10)
        self.assertEqual(self.calc.divide(20, -4), -5)
        self.assertEqual(self.calc.divide(-10, -10), 1)