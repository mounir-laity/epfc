def get_name_sex():
    while True:
        name = input("Please enter your name :\n")
        if not name:
            print("Please enter a name")
        else:
            break
    while True:
        sex = input("Please enter your sex (M/F) :\n")
        if not sex == "M" and not sex == "F":
            print("Please enter M if you're a male or F if you're a female !")
        else:
            break
    if sex == "M":
        print(f"Hello Mr {name}")
    else:
        print(f"Hello Ms {name}")


get_name_sex()
