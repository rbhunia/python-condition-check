def get_discount_percentage(membership_level: str) -> float:
    """
    Determines the discount percentage based on membership level.

    :param membership_level: The membership level of the customer
    :return: The discount percentage
    """
    membership_level = membership_level.lower()
    if membership_level == "gold":
        return 20.0
    elif membership_level == "silver":
        return 10.0
    elif membership_level == "bronze":
        return 5.0
    else:
        return 0.0


# Example usage:
membership_level = input("Enter your membership level (Gold, Silver, Bronze, Non-member): ")
discount = get_discount_percentage(membership_level)

if discount > 0:
    print(f"As a {membership_level.capitalize()} member, you get {discount}% off.")
else:
    print("You are not eligible for a discount.")
