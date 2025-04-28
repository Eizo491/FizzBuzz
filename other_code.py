import unittest
from test_code import fizzbuzz 

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_3(self):
        self.assertEqual(fizzbuzz(9), "fizz")

    def test_multiple_of_5(self):
        self.assertEqual(fizzbuzz(10), "buzz")

    def test_multiple_of_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "fizzbuzz")

    def test_neither(self):
        self.assertEqual(fizzbuzz(7), "7")

if __name__ == "__main__":
    unittest.main()
