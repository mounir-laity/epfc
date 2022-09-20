def index_max(liste: list):
    if not liste:
        return
    return liste.index(max(liste))


l = [2, 4, 5, 6, 9, -10, -20, 0.5]
print(index_max(l))
