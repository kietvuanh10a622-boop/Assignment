def login_system():
    
    correct_user = "Vu Anh Kiet"
    correct_pass = "2007"
    
   
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_user and password == correct_pass:
            print("Welcome")
            return  
        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect. You have {remaining} attempts left.")
            
    
    print("Access denied")


login_system()