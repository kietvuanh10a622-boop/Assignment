def cruise_cabin():
    cabin = input("Enter the cabin class (LUX, A, B, or C): ").upper()
    
    if cabin == "LUX":
        print("LUX: upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("A: above the car deck, equipped with a window.")
    elif cabin == "B":
        print("B: windowless cabin above the car deck.")
    elif cabin == "C":
        print("C: windowless cabin below the car deck.")
    else:
        print("Error: Invalid cabin class.")
cruise_cabin()
