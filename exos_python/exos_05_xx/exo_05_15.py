def len_separate(l):
    less_than_six = []
    more_than_five = []
    for element in l:
        less_than_six.append(element) if len(element) < 6 else more_than_five.append(
            element
        )
    return less_than_six, more_than_five


l = ["Jean", "Maximilien", "Brigitte", "Sonia", "Jean-Pierre", "Sandra"]

print(len_separate(l))
