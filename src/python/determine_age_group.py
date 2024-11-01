def determine_age_group(age: int) -> str:
    """
    Determines the age group for a given age.

    :param age: The age of the person
    :return: The age group classification
    """
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age <= 3:
        return "Toddler (0–3 years)"
    elif age <= 12:
        return "Child (4–12 years)"
    elif age <= 17:
        return "Teenager (13–17 years)"
    elif age <= 64:
        return "Adult (18–64 years)"
    else:
        return "Senior (65+ years)"


# Example usage:
try:
    age = int(input("Enter the age: "))
    age_group = determine_age_group(age)
    print(f"The person is categorized as: {age_group}")
except ValueError as e:
    print(e)
