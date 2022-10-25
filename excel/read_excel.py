
def read_notes(filename):
    with open(filename,"r") as file:
        for line in file:
            name, note = line.strip().split(";")
            print(f"{name} a eu la note {note}")


if __name__ == "__main__":
    read_notes("notes.csv")