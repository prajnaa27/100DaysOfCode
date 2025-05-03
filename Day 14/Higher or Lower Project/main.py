import random

import art
from game_data import data
print(art.logo)
current_score = 0
def compare(a,b):
    if a['follower_count'] > b['follower_count']:
        return 'A'
    else:
        return 'B'

def play_higher_or_lower(b=None):
    if b:
        a=b
    else:
        a = random.choice(data)
    b = random.choice(data)
    while a['name'] == b['name'] or a['follower_count'] == b['follower_count']:
        b = random.choice(data)
    print(f"Compare A {a['name']} a {a['description']} from {a['country']}")
    print(art.vs)
    print(f"Against B {b['name']} a {b['description']} from {b['country']}")
    user_answer=input("Who has more followers? Type 'A' or 'B': ")
    right_answer=compare(a,b)
    if user_answer == right_answer:
        global current_score
        current_score+= 1
        print(f"You are right! Current score : {current_score}")
        play_higher_or_lower(b)
    else:
        current_score
        print(f"Sorry that's wrong , Final score : {current_score}")
        exit(0)
play_higher_or_lower()
