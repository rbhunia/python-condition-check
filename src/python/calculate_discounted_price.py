def calculate_discounted_price(total_amount: float) -> float:
    """
    Calculates the discounted price based on the total purchase amount.

    :param total_amount: The total amount of the purchase
    :return: The total amount after applying the discount
    """
    if total_amount < 50:
        discount = 0
    elif 50 <= total_amount <= 100:
        discount = 0.10  # 10% discount
    else:  # total_amount > 100
        discount = 0.20  # 20% discount

    discounted_price = total_amount * (1 - discount)
    return discounted_price


# Example usage:
try:
    total_amount = float(input("Enter the total purchase amount: $"))
    final_price = calculate_discounted_price(total_amount)
    print(f"The final price after discount is: ${final_price:.2f}")
except ValueError:
    print("Please enter a valid numerical value for the total amount.")
