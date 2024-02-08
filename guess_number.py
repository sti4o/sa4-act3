number = 10

print("I'm thinking of a number...")
while True:
    guess = input("What number am I thinking of? (Enter 'q' to quit): ")
    
    if guess.lower() == 'q':
        print(f"You've chosen to quit. The number was {number}.")
        break
    
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break  # Exit the loop if the guess is correct
        elif guess < number:
            print("Incorrect. Your guess is too low. Try again.")
        else:  # This means guess > number
            print("Incorrect. Your guess is too high. Try again.")
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
