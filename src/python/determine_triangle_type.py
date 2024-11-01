def determine_triangle_type(a: float, b: float, c: float) -> str:
    """
    Determines the type of triangle based on the side lengths.

    :param a: Length of the first side
    :param b: Length of the second side
    :param c: Length of the third side
    :return: The type of triangle: "Equilateral", "Isosceles", or "Scalene"
    """
    # Check if the inputs can form a triangle
    if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
        return "Not a valid triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"


# Example usage:
try:
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    triangle_type = determine_triangle_type(a, b, c)
    print(f"The triangle is: {triangle_type}")
except ValueError:
    print("Please enter valid numerical values for the side lengths.")
