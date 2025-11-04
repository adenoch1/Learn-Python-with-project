# secret bidding
import time
import os

bidding_details = {}
winner = ""
highest_bid = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Enter your name: ").strip()

    while True:
        bid = float(input("Enter your bid amount: "))
        try:
            bid = float(bid)
            break
        except ValueError:
            print("Type a number pls. ")

    new_bidders = input("Are there any more bidders? (yes/no): ").lower().strip()
    if new_bidders == "yes":
        print("New bidding comming.... Pls wait")
        time.sleep(1)
    elif new_bidders == "no":
        print("Thank you all for bidding.")
        time.sleep(1)
        break

    bidding_details[name] = bid

for key, value in bidding_details.items():
    if value > highest_bid:
        highest_bid = value
        winner = key

os.system('cls' if os.name == 'nt' else 'clear')
print(f"The winner is {winner} with a bid of ${highest_bid}")
