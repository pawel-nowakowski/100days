from os import system
from auction_logo import logo
print(logo)
while True:
    system('cls')
    name = input("What is your name? \n")
    bid = input("What is your bid? \n")
    auction = dict()
    auction[name] = bid
    winner_k = max(auction, key=auction.get)
    winner_v = max(auction.values())
    bidding = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if bidding == 'no':
        break
    else:
        continue

print(f"The winner is {winner_k} with {winner_v}$ bid.")