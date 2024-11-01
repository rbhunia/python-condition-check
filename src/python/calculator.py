from random import choice


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error! Division by zero.")
    return x / y

def calculator():
    print("Please select operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = int(input("Please enter your choice (1/2/3/4)"))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid input. Please enter a nuber b/w 1 to 4")
            return

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        print("Do you want to try again?")
        retry = input("Please enter (y/n)")

        if retry == "n" or retry == "N":
            break
        elif retry not in ["Y", "N", "y", "n"]:
            raise ValueError("Invalid input")


try:
    calculator()
except ValueError as e:
    print(e)