
numbers = []

while True:
  
    user_input = input("Enter a number (press Enter to quit): ")
    
    
    if user_input == "":
        break
    
    
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")


if len(numbers) > 0:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")