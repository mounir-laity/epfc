def get_sqrt():
    try:
        number = int(input("Entrez un nombre : \n"))
        return number**0.5
    except Exception:
        return "La racine carrée ne peut être calculée"


print(get_sqrt())
