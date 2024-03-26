# PalindromeChecker.py
class PalindromeChecker:
    """
    This class provides methods to check if a string is a palindrome.
    """
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Check if a given string is a palindrome.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the input string is a palindrome, False otherwise.
        """
        return s == s[::-1]
