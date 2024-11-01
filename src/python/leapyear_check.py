def is_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    return False

year_input = int(input("Please enter the year: "))
print(is_leap_year(year_input))