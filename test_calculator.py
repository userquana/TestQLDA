import unittest
import pytest
from calculator import Calculator
import tkinter as tk

class TestCalculator(unittest.TestCase):

    def setUp(self):
        root = tk.Tk()
        root.withdraw() 
        self.calc = Calculator(root)

    def test_add_basic(self):
        self.calc.expression = "5"
        self.calc.add_operator("+")
        self.calc.add_to_expression("3")
        self.calc.calculate()
        self.assertEqual(self.calc.expression, "8")

    def test_add_with_zero_boundary(self):
        self.calc.expression = "0"
        self.calc.add_operator("+")
        self.calc.add_to_expression("9")
        self.calc.calculate()
        self.assertEqual(self.calc.expression, "9")

    def test_subtract(self):
        self.calc.expression = "10"
        self.calc.add_operator("-")
        self.calc.add_to_expression("4")
        self.calc.calculate()
        self.assertEqual(self.calc.expression, "6")

    def test_multiply(self):
        self.calc.expression = "6"
        self.calc.add_operator("×")
        self.calc.add_to_expression("3")
        self.calc.calculate()
        self.assertEqual(self.calc.expression, "18")


    def test_divide(self):
        self.calc.expression = "12"
        self.calc.add_operator("÷")
        self.calc.add_to_expression("3")
        self.calc.calculate()
        self.assertEqual(self.calc.expression, "4.0")


    def test_divide_by_zero(self):
        self.calc.expression = "10"
        self.calc.add_operator("÷")
        self.calc.add_to_expression("0")
        with self.assertRaises(Exception):   
            self.calc.calculate()

    def test_square_root(self):
        self.calc.expression = "16"
        self.calc.square_root()
        self.assertEqual(self.calc.expression, "4.0")

    def test_square(self):
        self.calc.expression = "5"
        self.calc.square()
        self.assertEqual(self.calc.expression, "25")

if __name__ == '__main__':
    unittest.main()
