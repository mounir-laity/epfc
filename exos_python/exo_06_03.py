from math import pi


def calc_period():
    length = float(input("Please enter the length of the pendulum :\n"))
    try:
        if length <= 0:
            raise ValueError
        g = 9.806
        return 2 * pi * (length / g) ** 0.5
    except ValueError:
        print("The length must be greater than 0 !")


print(f"The period of the pendulum is {calc_period()} seconds")
