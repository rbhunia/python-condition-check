def character_checker(char: str) -> str:
    """
    Checks if the input character is a vowel, consonant, or other character.

    :param char: The character to check
    :return: The classification of the character
    """
    if len(char) != 1:
        return "Input must be a single character"

    vowels = "aeiouAEIOU"

    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special symbol"


# Example usage:
char = input("Enter a single character: ")

result = character_checker(char)
print(f"The character '{char}' is a {result}.")
