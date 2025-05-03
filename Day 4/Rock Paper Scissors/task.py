import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choices=[rock,paper,scissors]
user_choice=int(input("What do you Choose?\n Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice=random.randint(0,2)
if user_choice>=0 and user_choice <=2:
    print(f"You chose:\n{game_choices[user_choice]}")
    print(f"Computer chose:\n{game_choices[computer_choice]}")

    if user_choice == computer_choice:
        print("Its a draw")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (
            user_choice == 2 and computer_choice == 0):
        print("You lose")
    else:
        print("You won")
else:
    print("Invalid option")

