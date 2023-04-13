import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

# while loop and user input
while True:
    user_input = input("Type rock/paper/scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0: rock, 1: paper, 2: scissors
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}. ")

# game variations inside the if statement
    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'scissors':
        print("It's a draw.")
    elif user_input == 'paper' and computer_pick == 'paper':
        print("It's a draw.")
    elif user_input == 'rock' and computer_pick == 'rock':
        print("It's a draw.")
    else:
        print("You lost")
        computer_wins += 1

# results outcome
print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
