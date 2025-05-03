import random
import art


def number_guessing_game():
    print(art.logo)
    print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.\n")
    number=random.randint(1,100)
    print(f"the number is {number}")

    difficulty=input("Choose a difficulty. Type 'easy' or 'hard'\n")
    if difficulty=='easy':
        attempts=10
    else:
        attempts=5

    while attempts!=0:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        guess=int(input("Make a guess\n"))
        if guess<number:
            print("Too low")
            if attempts!=1:
                print("Guess again.")
            else:
                print(f"You have run out of guesses , You lose\nThe right answer was {number}")
            attempts-=1
        elif guess>number:
            print("Too high")
            if attempts != 1:
                print("Guess again.")
            else:
                print(f"You have run out of guesses , You lose\nThe right answer was {number}")
            attempts -= 1
        elif guess==number:
            print("Congratulations! It's the right guess")
            break
    choice=input("Do you wanna play again.\nType 'y' for yes and 'n' for no\n").lower()
    if choice=='y':
        number_guessing_game()
    else:
        exit(0)
number_guessing_game()

