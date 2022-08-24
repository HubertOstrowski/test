import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
if user_action == computer_action:
    print("Wybraliście to samo remis")
elif user_action == "scissors":
    if computer_action == "rock":
        print("Kamien pokonuje nozyce")
    else:
        print("Nozyce pokonuja papier")
elif user_action == "paper":
    if computer_action == "rock":
        print("kamien pokonany przez papier")
    else:
        print("nożyce pokonuja papier")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Kamien niszczy nozyce")
    else:
        print("Papier pokonuje kamien")