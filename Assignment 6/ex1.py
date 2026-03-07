numbers = []

while True:
    user_input = input("Enter a number: ")
    
    if user_input == "":
        break
    
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        pass

numbers.sort(reverse=True)

print("The five greatest numbers are:")
print(numbers[:5])