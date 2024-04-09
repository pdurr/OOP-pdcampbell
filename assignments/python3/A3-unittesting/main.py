from MorseCodeConverter import MorseCodeConverter
from PalindromeChecker import PalindromeChecker


class MorseCodePalindromeChecker:
    """
    Check if a string's Morse code representation is a palindrome.
    """

    _converter: MorseCodeConverter
    _checker: PalindromeChecker

    def __init__(self) -> None:
        """
        Initialize the MorseCodePalindromeChecker class.
        """
        self._converter = MorseCodeConverter()
        self._checker = PalindromeChecker()

    def is_morse_code_palindrome(self, s: str) -> bool:
        """
        Check if a given string (or its Morse code representation) is a palindrome.

        Args:
            s (str): The input string to check.

        Returns:
            bool: T if the input string's Morse code representation is a palindrome, F otherwise.
        """
        morse_code = self._converter.convert_to_morse(s)
        return self._checker.is_palindrome(morse_code)

    @property
    def converter(self) -> MorseCodeConverter:
        """
        Get the MorseCodeConverter instance used for converting strings to Morse code.

        Returns:
            MorseCodeConverter: The MorseCodeConverter instance.
        """
        return self._converter

    @property
    def checker(self) -> PalindromeChecker:
        """
        Get the PalindromeChecker instance used for checking if a string is a palindrome.

        Returns:
            PalindromeChecker: The PalindromeChecker instance.
        """
        return self._checker


if __name__ == "__main__":
    # Input string
    input_string: str = input().strip()

    # Create an instance of the MorseCodePalindromeChecker class
    checker: MorseCodePalindromeChecker = MorseCodePalindromeChecker()

    # Check if input string is a Morse Code Palindrome
    if any(char.isalnum() for char in input_string):
        if checker.is_morse_code_palindrome(input_string):
            print(1)
        else:
            print(0)
    else:
        print(0)
