# MorseCodeConverter.py
class MorseCodeConverter:
    """
    This class provides methods to convert strings to Morse code.
    """

    _morse_code_dict: dict[str, str]

    def __init__(self) -> None:
        """
        Initialize the MorseCodeConverter class.
        """
        self._morse_code_dict = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
        }

    def convert_to_morse(self, s: str) -> str:
        """
        Convert a given string to Morse code.

        Args:
            s (str): The input string to convert.

        Returns:
            str: The Morse code representation of the input string.
        """
        morse_code = ""
        for char in s:
            if char.isalnum():
                morse_code += self._morse_code_dict[char.upper()]
        return morse_code

    @property
    def morse_code_dict(self) -> dict[str, str]:
        """
        Get the dictionary containing the mapping of characters to Morse code.

        Returns:
            dict[str, str]: The dictionary mapping characters to Morse code.
        """
        return self._morse_code_dict
