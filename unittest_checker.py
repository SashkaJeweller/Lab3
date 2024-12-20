import unittest
from roman_checker import is_valid_roman

class TestRomanNumerals(unittest.TestCase):
    def test_valid_romans(self):
        valid_romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M", "MM", "MMM"]
        for roman in valid_romans:
            with self.subTest(roman=roman): 
                self.assertTrue(is_valid_roman(roman))

    def test_invalid_romans(self):
        invalid_romans = ["IIII", "VV", "XXXX", "IL", "IC", "MCMXCIVV", "MMMM"]
        for roman in invalid_romans:
            with self.subTest(roman=roman): 
                self.assertFalse(is_valid_roman(roman))

if __name__ == "__main__":

    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("\nВсе тесты прошли успешно!")
    else:
        print("\nНекоторые тесты не прошли.")
