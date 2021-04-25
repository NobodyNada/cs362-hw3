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


year = input("Enter a year: ")
if is_leap_year(int(year)):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))

