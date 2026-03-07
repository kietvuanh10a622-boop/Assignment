seasons = ("Winter", "Spring", "Summer", "Autumn")

try:
    month = int(input("Enter month : "))

    if 1 <= month <= 12:
      
        index = (month % 12) // 3
        print(f"The season is {seasons[index]}.")
    else:
        print("Please enter a number between 1 and 12.")
        
except ValueError:
    print("Invalid input. Please enter a whole number.")
    