def add_mult_3_and_5(min, max):
    sum = 0
    for i in range(min, max + 1):
        if i % 3 == 0 and i % 5 == 0:
            sum += i
    return sum


def add_mult_3_or_5(min, max):
    sum = 0
    for i in range(min, max + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print(add_mult_3_and_5(0, 40))
print(add_mult_3_or_5(0, 40))
