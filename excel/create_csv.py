from random import randint
from read_excel import read_notes

possible_names = ["Mounir", "Julien", "Fouad", "Myriam"]
with open("notes2.csv", "w") as file:
    for name in possible_names:
        note = randint(0,20)
        file.write(f"{name};{note}\n")
        
if __name__ == "__main__":
    read_notes("notes2.csv")