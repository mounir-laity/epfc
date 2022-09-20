def get_area_perimeter():
    a = float(input("Please enter the length of the first side :\n"))
    b = float(input("Please enter the length of the second side :\n"))
    c = float(input("Please enter the length of the third side :\n"))
    perimeter = a + b + c
    demi = perimeter / 2
    area = (demi * (demi - a) * (demi - b) * (demi - c)) ** 0.5
    return perimeter, area


print(get_area_perimeter(10, 12, 13))
print(get_area_perimeter(40, 25, 31))
