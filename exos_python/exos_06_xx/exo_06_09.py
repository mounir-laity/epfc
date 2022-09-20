def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


print(is_leap_year(2000))
print(is_leap_year(2022))
print(is_leap_year(2077))
print(is_leap_year(2020))
print(is_leap_year(0))
