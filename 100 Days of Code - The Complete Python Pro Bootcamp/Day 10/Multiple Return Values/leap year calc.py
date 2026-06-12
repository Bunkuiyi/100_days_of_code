def is_leap_year(year):
    """Takes a year and returns if that year is a leap year or not."""
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False

output = is_leap_year(2020)
print(output)