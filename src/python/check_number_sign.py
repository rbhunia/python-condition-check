def check_number_sign(number: int) -> str:
    """
    Checks if the given number is positive, negative, or zero.

    :param number: The number to check
    :return: A string indicating whether the number is "Positive", "Negative", or "Zero"
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


# Example usage:
try:
    number = int(input("Enter an integer: "))
    result = check_number_sign(number)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid integer.")
