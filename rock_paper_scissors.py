import random

user_wins = 0
computer_wins = 0

running = True
while running:
    user_input = input("Type Rock, Paper, or Scissors. Type Q to quit: ").lower()
    if user_input == "q":
        running = False

    if user_input not in ["rock", "paper", "scissors"]:
        continue
