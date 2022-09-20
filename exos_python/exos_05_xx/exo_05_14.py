def list_odd_even(l):
    odds = []
    evens = []
    for element in l:
        evens.append(element) if element % 2 == 0 else odds.append(element)
    return odds, evens


l = [-10, 0, 3, 15, 123, 456, 799, -42, -7]
print(list_odd_even(l))
