#!/usr/bin/env python3

def is_leap_year(year):
    if year % 4 != 0:
        # If not divisible by 4, not a leap year:
        return False
    elif year % 100 != 0:
        # If divisible by 4 but not 100, a leap year
        return True    
    elif year % 400 != 0:
        # If divisible by 100 but not 400, not a leap year
        return False
    else:
        # If divisible by 400, a leap year
        return True

while True:
    # Read the year from standard input
    try:
        year = input("Enter a year: ")
    except EOFError:
        # EOF, just exit
        break

    # Convert to integer
    try:
        year = int(year)
    except ValueError:
        print("Please enter a valid year.")
        continue

    if is_leap_year(int(year)):
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))

    break
