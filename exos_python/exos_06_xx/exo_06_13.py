def convert_note():
    note = float(input("Please enter the obtained note :\n"))
    total = float(input("Please enter the maximum note :\n"))
    percentage = note / total
    if percentage >= 0.8:
        return "A"
    if percentage >= 0.6:
        return "B"
    if percentage >= 0.5:
        return "C"
    else:
        return "D"


print(convert_note())
