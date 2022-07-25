import re
from dictionary import eng_to_ar, ar_to_eng


def convert_gb(gibberish:str):
    """converts gibberish text to the language it was meant to be in

    Args:
        gibberish (str): the string to be converted
    """
    # Regex pattern that checks for arabic characters
    arabic_pattern = "^[\u0621-\u064A0-9 ]+$" 

    # Matching gibberish text with arabic pattern
    arabic_match = re.match(arabic_pattern, gibberish)

    # Storing a boolean value of whether or not gibberish text has arabic chars
    is_arabic = bool(arabic_match)

    # Non-gibberish string to be return by function
    non_gibberish = ""

    if is_arabic:
        # If true, then the gibberish text is in ar, which is meant to be in en
        for letter in gibberish: # Iterate through each letter in gibberish
                # Append true value of gibberish to non-gibberish text
                if letter == ' ':
                    non_gibberish += ' '
                elif letter.isnumeric():
                    non_gibberish += letter
                else:
                    non_gibberish += ar_to_eng.get(letter)
    elif gibberish.isascii():
        # If true, then the gibberish text is in en, which is meant to be in ar
        # Same explanation as loop above
        for letter in gibberish:
            if letter == ' ':
                non_gibberish += ' '
            elif letter.isnumeric():
                non_gibberish += str(letter)
            else:
                non_gibberish += eng_to_ar.get(letter)

    return non_gibberish