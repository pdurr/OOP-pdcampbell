import unittest
from hypothesis import given
import hypothesis.strategies as st
from MorseCodeConverter import MorseCodeConverter
from PalindromeChecker import PalindromeChecker


class TestMorseCodePalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.converter = MorseCodeConverter()
        self.checker = PalindromeChecker()

    def test_convert_to_morse(self) -> None:
        # Test converting a simple string to Morse code
        self.assertEqual(self.converter.convert_to_morse("hello"), "......-...-..---")

        # Test converting a string with non-alphanumeric characters to Morse code
        self.assertEqual(
            self.converter.convert_to_morse("hello!123"),
            "......-...-..---.----..---...--",
        )

    def test_is_palindrome(self) -> None:
        # Test Morse code palindrome
        self.assertTrue(self.checker.is_palindrome("....-.-.-...."))
        self.assertTrue(self.checker.is_palindrome("-----..-----"))
        self.assertTrue(self.checker.is_palindrome("----..-.-.-..----"))

        # Test non-palindrome Morse code
        self.assertFalse(self.checker.is_palindrome("....-.-.-..."))
        self.assertFalse(self.checker.is_palindrome("-----..----"))
        self.assertFalse(self.checker.is_palindrome("----.--.--.-"))

        # Test empty string
        self.assertTrue(self.checker.is_palindrome(""))

    @given(st.text())
    def test_is_palindrome_with_generated_data(self, input_data: str) -> None:
        """
        Test is_palindrome method with generated data using hypothesis.
        """
        # Test is_palindrome method with generated data
        # Test is_palindrome method with generated data
        result = self.checker.is_palindrome(input_data)
        # Add assertions based on the behavior of is_palindrome method
        self.assertIsInstance(result, bool)  # Assert that result is a boolean value
        # input_data is empty or has a single character, it should always be a palindrome
        if len(input_data) <= 1:
            self.assertTrue(result)
        # Assert that palindrome remains unchanged when reversed
        if result:
            self.assertEqual(input_data, input_data[::-1])
        else:
            # Assert that non-palindrome does not remain unchanged when reversed
            self.assertNotEqual(input_data, input_data[::-1])


if __name__ == "__main__":
    unittest.main()
