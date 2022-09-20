from statistics import mean

notes = []
count = 0
while True:
    note = float(input("Please enter a note :\n"))
    if note < 0:
        print(notes)
        break
    notes.append(note)
    count += 1
    print(f"Nombre de notes : {count}")
    print(f"Maximum des notes : {max(notes)}")
    print(f"Minimum des notes : {min(notes)}")
    print(f"Moyenne des notes : {mean(notes)}")
