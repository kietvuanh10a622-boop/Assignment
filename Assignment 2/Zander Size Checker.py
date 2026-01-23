def check_zander():
    limit = 42
    length = float(input("Enter the length of the zander in centimeters: "))
    
    if length >= limit:
        print("The fish meets the size limit. Enjoy your catch!")
    else:
        difference = limit - length
        print(f"Please release the fish back into the lake.")
        print(f"The fish is {difference:.1f} cm below the size limit.")
        
check_zander()
