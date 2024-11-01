def determine_day_of_week(day_number: int) -> str:
    """
    Determines the day of the week based on a provided number (1-7).

    :param day_number: The day number (1-7)
    :return: The corresponding day of the week
    """
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    return days_of_week.get(day_number, "Invalid day number. Please enter a number between 1 and 7.")


# Example usage:
try:
    day_number = int(input("Enter a number (1-7): "))
    day_of_week = determine_day_of_week(day_number)
    print(f"The day of the week is: {day_of_week}")
except ValueError:
    print("Please enter a valid integer between 1 and 7.")
