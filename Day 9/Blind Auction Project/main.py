# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import os
from art import logo
print(logo)
print("Welcome to the secret auction program.\n")
other_bidders=True
bidders={}
def findHighestBidder(bidders):
    max_bid=0
    winner=''
    for name,bid in bidders.items():
        if bid>max_bid:
            max_bid=bid
            winner=name
    print(f"The winner is {winner} with a bid of {max_bid}")

while other_bidders==True:
    name=input("What is your name?\n")
    bid=int(input("What's your bid?\n Rs."))
    bidders[name]=bid
    otherspresent=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    print("\n" * 100)
    other_bidders=True if otherspresent=='yes' else findHighestBidder(bidders)


