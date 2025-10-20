# test_calculator.py
import unittest
from calculator import add, greet

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_greet(self):
        self.assertEqual(greet("Gus"), "Hello, Gus!")
        self.assertNotEqual(greet("Gus"), "Hi Gus")

if __name__ == "__main__":
    unittest.main()