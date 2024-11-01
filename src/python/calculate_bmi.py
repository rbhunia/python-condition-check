def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculates the Body Mass Index (BMI) given weight and height.

    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: The calculated BMI
    """
    return weight / (height ** 2)


def categorize_bmi(bmi: float) -> str:
    """
    Categorizes the BMI value into one of the categories: Underweight, Normal weight, Overweight, Obese.

    :param bmi: The calculated BMI
    :return: A string representing the BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:  # bmi >= 30
        return "Obese"


# Example usage:
try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")
except ValueError:
    print("Please enter valid numerical values for weight and height.")
