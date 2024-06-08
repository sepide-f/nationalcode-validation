import unittest

from nationalcode_validatorr.main import national_code_validator

class TestNationalCodeValidator(unittest.TestCase):
    def test_valid_code(self):


        valid_code = "1234567890"
        result = national_code_validator(valid_code)
        self.assertEqual(result, (True, "Region Name"))

    def test_invalid_code(self):


        invalid_code = "123456789"
        result = national_code_validator(invalid_code)
        self.assertEqual(result, "please enter 10 digits")


        invalid_code = "abcdefghij"
        result = national_code_validator(invalid_code)
        self.assertEqual(result, "please enter a digit")


if __name__ == '__main__':
    unittest.main()
