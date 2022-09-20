for i in range(1, 21):
    star = ""
    mult = 7 * i
    if mult % 3 == 0:
        star = "*"
    print(f"{mult}{star}", end=" ")
