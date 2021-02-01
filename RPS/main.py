import random

while True:
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()
    print("computer: " + computer)
    print("player: " + player)
    if computer==player:
        print("computer: " + computer)
        print("player: " + player)
        print ("tied")
    elif computer == "rock" and player == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print ("computer won")
    elif computer == "rock" and player == "paper":
        print("computer: " + computer)
        print("player: " + player)
        print ("player won")
    elif computer == "paper" and player == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print ("computer won")
    elif computer == "paper" and player == "scissors":
        print("computer: " + computer)
        print("player: " + player)
        print ("player won")
    elif computer == "scissors" and player == "rock":
        print("computer: " + computer)
        print("player: " + player)
        print ("player won")
    elif computer == "scissors" and player == "paper":
        print("computer: " + computer)
        print("player: " + player)
        print ("computer won")
    a = input("Do you want to play(yes/no): ").lower()
    if (a != "yes"):
        break
print("It was nice playing with You!!")