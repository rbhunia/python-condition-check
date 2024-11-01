def is_prime(number: int) -> bool:
    """
    Checks if the given number is a prime number.

    :param number: The number to check
    :return: True if the number is prime, False otherwise
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


# Example usage:
try:
    number = int(input("Enter an integer: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
