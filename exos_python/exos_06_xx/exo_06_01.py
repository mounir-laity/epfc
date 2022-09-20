while True:
    try:
        mph = float(input("Please enter your speed in mph :\n"))
        print(f"Speed in km/h : {mph*1609/1000}")
        print(f"Speed in m/s : {mph*1609/3600}")
        break
    except ValueError:
        print("Please enter a number !")
