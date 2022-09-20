import calendar


def nom_mois(n):
    if n < 1 or n > 12:
        raise ValueError("The month must be between 1 and 12 !")
    return calendar.month_name[n]


print(nom_mois(10))
print(nom_mois(1))
print(nom_mois(12))
print(nom_mois(0))
