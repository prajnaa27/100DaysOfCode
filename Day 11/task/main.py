import art
import random

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
def find_winner(user_cards,computer_cards):
    if 11 in user_cards and sum(user_cards)>21:
        user_cards.remove(11)
        user_cards.append(1)
    if 11 in computer_cards and sum(computer_cards)>21:
        computer_cards.remove(11)
        computer_cards.append(1)
    print(f"Your final hand : {user_cards}")
    print(f"Computer's final hand : {computer_cards}")
    sum_user_cards = sum(user_cards)
    sum_computer_cards = sum(computer_cards)
    if sum_user_cards > sum_computer_cards and sum_user_cards <= 21:
        print("You win")
        play_blackjack()
    elif sum_computer_cards>21:
        print("Opponent went over !! You win")
        play_blackjack()
    elif sum_user_cards==sum_computer_cards:
        print("Its a draw")
        play_blackjack()
    else:
        print("You lose")
        play_blackjack()

def start(user_cards,computer_cards):
    get_another_card = input("Type 'y' to get another card, type 'n' to pass\n")
    if get_another_card == 'n':
        find_winner(user_cards, computer_cards)
    elif get_another_card == 'y':
        new_card = random.choice(numbers)
        user_cards.append(new_card)
        if sum(user_cards) > 21:
            print(f"Your final hand: {user_cards}, current_score{sum(user_cards)}")
            print(f"Computer's final hand: {computer_cards}")
            print("You went over! It's a bust")
            play_blackjack()
        else:
            print(f"Your cards: {user_cards}, current_score{sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
            start(user_cards,computer_cards)

def play_blackjack():
    print(art.logo)
    choice = input("Do you want to play a game of Blackjack?\n Type 'y' or 'n'\n").lower()
    print(art.logo)
    while choice == 'y':
        user_cards = random.choices(numbers, k=2)
        computer_cards = random.choices(numbers, k=2)
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(numbers))
            if 11 in computer_cards and sum(computer_cards) > 21:
                computer_cards.remove(11)
                computer_cards.append(1)
        print(f"Your cards: {user_cards}, current_score{sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        start(user_cards,computer_cards)

            # find_winner(user_cards, computer_cards)
    exit(0)

play_blackjack()