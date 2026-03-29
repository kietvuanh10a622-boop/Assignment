numbers = []

while True:
    data = input("Enter a number: ")
    
    if data == "":
        break
        
    try:
        num = float(data)
        numbers.append(num)
    except ValueError:
        print("Error, Please type only number.")

numbers.sort(reverse=True)

top_five = numbers[:5]

print("\n--- Result ---")
print(f"5 largest to loweest number: {top_five}")