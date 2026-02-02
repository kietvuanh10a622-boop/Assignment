import random

def guessing_game():
  
    secret_number = random.randint(1, 10)
    
    print("I have chosen a number between 1 and 10. Can you guess it?")

   
    while True:
        guess = int(input("Enter your guess: "))

        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Correct!")
           
            break


guessing_game()