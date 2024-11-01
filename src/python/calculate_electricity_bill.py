def calculate_electricity_bill(usage_kwh: float) -> float:
    """
    Calculates the electricity bill based on the usage in kWh.

    :param usage_kwh: The usage in kilowatt-hours (kWh)
    :return: The total electricity bill
    """
    if usage_kwh < 0:
        raise ValueError("Usage cannot be negative")

    if usage_kwh <= 100:
        bill = usage_kwh * 0.50
    elif usage_kwh <= 300:
        bill = (100 * 0.50) + ((usage_kwh - 100) * 0.75)
    else:
        bill = (100 * 0.50) + (200 * 0.75) + ((usage_kwh - 300) * 1.00)
    return bill


# Example usage:
try:
    usage_kwh = float(input("Enter the electricity usage in kWh: "))
    total_bill = calculate_electricity_bill(usage_kwh)
    print(f"The total electricity bill is: ${total_bill:.2f}")
except ValueError as e:
    print(e)
