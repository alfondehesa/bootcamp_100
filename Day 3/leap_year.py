# This program asks the user for a year, and returns wether the year is a leap year or not.
# A leap year is:
#   Divisible by 4
#   Except years that are divisible by 100
#   Unless the year is also divisible by 400


def is_leap(year: int):
    is_leap_year = "Error"

    if year % 4 == 0:
        if year % 100 != 0:
            is_leap_year = "Leap year."
        elif year % 400 == 0:
            is_leap_year = "Leap year."
    else:
        is_leap_year = "Not leap year."

    return is_leap_year


print(is_leap(int(input("Enter your year: "))))
