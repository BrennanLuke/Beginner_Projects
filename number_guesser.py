import random

# User defined number range
top_of_range = input("Type a number: ")

# Converts str into int
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

# Prompts user to resubmit if the number is out of program's range
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()


random_number = random.randint(0, top_of_range)  # Generates a random number over 0 and at or under user's submission
                                                    ## r = random.randint(-5, 12)  # random number from x, to x.  ##
running = True  # Running Flag
guesses = 0  # User guesses
score = 0

while running:
    guesses += 1  # Increments each guess number
    user_guess = input("Make a guess: ")

    # Converting string to integer
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time: ")
        continue

    # Prompts user if right or wrongs guess
    if user_guess == random_number:
        print("Congrats! You guessed the number!")
        running = False  # End flag
    else:  # Gives user hints about number range
        if user_guess > random_number:
            print("Too high!")
        elif user_guess < random_number:
            print("Too low!")
        else:
            print("Sorry, you guessed the wrong number!")

    # Calculates the score
    score = score + user_guess/4*100


print("You guessed the number in", guesses, "guesses!")
