running = True
while running:  # Loop allowing replay

    # Welcome screen
    print("Welcome to Video Game Quotes!"
          "\nGuess which quote belongs to each character.\n")

    # Begin playing?
    playing = input("............Are you ready? (y)yes or (n)no\n")

    if playing.lower() != "y":
        quit()

    print("### Okay! Let's play :) ###\n")
    score = 0

    # Question 1
    user_answer = input("1. Who said: \"It’s time to kick ass and chew bubble gum… and I’m all outta gum\"?")
    answer = "duke nukem"
    if user_answer.strip() and all(word.lower() in answer.lower().split() for word in user_answer.lower().split()):
        print("You are correct!\n")
        score += 1
    else:
        print("That was incorrect.\n")

    # Question 2
    user_answer = input("2. Who said: \"*grunts angrily* Boy\"?")
    answer = "kratos"
    if user_answer.strip() and all(word.lower() in answer.lower().split() for word in user_answer.lower().split()):
        print("You are correct!\n")
        score += 1
    else:
        print("That was incorrect.\n")

    # Question 3
    user_answer = input("3. Who said: \"Are you a boy or a girl?\"?")
    answer = "professor oak"
    if user_answer.strip() and all(word.lower() in answer.lower().split() for word in user_answer.lower().split()):
        print("You are correct!\n")
        score += 1
    else:
        print("That was incorrect.\n")

    # Question 4
    user_answer = input("4. Who said: \"Does this unit have a soul?\"?")
    answer = "legion"
    if user_answer.strip() and all(word.lower() in answer.lower().split() for word in user_answer.lower().split()):
        print("You are correct!\n")
        score += 1
    else:
        print("That was incorrect.\n")

    # Question 5
    user_answer = input("5. Who said: \"A sword wields no strength unless the hands that holds it has courage.\"?")
    answer = "hero's spirit hero time"
    if user_answer.strip() and all(word.lower() in answer.lower().split() for word in user_answer.lower().split()):
        print("You are correct!\n")
        score += 1
    else:
        print("That was incorrect.\n")

    # Final Scores
    print("You answered " + str(score) + " correct questions")
    print
