def get_triangle_type():
    a = float(input("Please enter the length of the first side :\n"))
    b = float(input("Please enter the length of the second side :\n"))
    c = float(input("Please enter the length of the third side :\n"))
    if a >= b + c or b >= a + c or c >= a + b:
        return "Pas un triangle"
    if a == b and a == c:
        return "Triangle équilatéral"
    if (
        a**2 == (b**2 + c**2)
        or b**2 == (a**2 + c**2)
        or c**2 == (a**2 + b**2)
    ):
        if a == b or a == c or b == c:
            return "Triangle rectangle isocèle"
        return "Triangle rectangle"
    if a == b or a == c or b == c:
        return "Triangle isocèle"
    return "Triangle quelconque"


print(get_triangle_type())
