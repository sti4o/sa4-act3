number = 10
max_guesses = 5  # Set the maximum number of guesses allowed

print("I'm thinking of a number...")
while max_guesses > 0:
    guess = input(f"What number am I thinking of? (Enter 'q' to quit): You have {max_guesses} guesses left. ")
    
    if guess.lower() == 'q':
        print(f"You've chosen to quit. The number was {number}.")
        break
    
    try:
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break  # Exit the loop if the guess is correct
        elif guess < number:
            print("Incorrect. Your guess is too low.")
        else:  # This means guess > number
            print("Incorrect. Your guess is too high.")
        
        max_guesses -= 1  # Decrement the number of remaining guesses
        if max_guesses == 0:
            print(f"Sorry, you've run out of guesses. The number was {number}.")
            break
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
