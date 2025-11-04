# higher lower game

"""
write a function to clear your screen
write a function to play game and return a score
In the play game function, do the following:
shuffle the data
print logo
Give a score equals zero to track score
Loop through the data for about 6 or more times to select dictionaries to format.
Define two items that will be used throughout the game.
Format the items to print and compare their name, description and country, and
In a while loop, allow the player to guess who has the highest followers.
Use the while loop to check to make sure players give a valid answer
Print the name and followers of each player in millions
Compare the followers of the two selected entries and get the one with the highest followers
For every correct guess, give the player a score
Before the end of end each loop, use input function to allow player to press enter to continue and clear the screen.
print a game over message and display the final score, and return score

Write a function to get a yes & return True or no & return False to play game or not.
write a main function to make the game repetitive, call other functions and actually play the game.
"""

import os
import random
from images import logo, vs
from higher_data import data


def clear_screen():
    """Use to clear screen before playing each game"""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    """Play game and return a score"""
    score = 0
    random.shuffle(data)
    print(logo)

    # loop through data and create two items
    # for i in (len(data) - 1)
    for i in range(6):
        item_a = data[i]
        item_b = data[i + 1]

        # format the items to get and compare name, description and country
        print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
        print()
        print(vs)
        print()
        print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")

        # Guess followers
        while True:
            guess = input("Who has the highest followers? 'A' or 'B': ").upper().strip()
            if guess in ['A', 'B']:
                break
            else:
                print("Invalid input! Try again.")

        a_followers = item_a["follower_count"]
        b_followers = item_b["follower_count"]

        print(f"{item_a['name']}: {a_followers}M | {item_b['name']}: {b_followers}M")

        if a_followers > b_followers:
            correct = 'A'
        elif a_followers < b_followers:
            correct = 'B'
        else:
            correct = None   # tie

        if guess == correct:
            score += 1
            print(f"Correct guess! | Score: {score}")
        elif guess == None:
            print(f"It's a draw! | Score: {score}")
        else:
            print(f"Wrong guess! | Score: {score}")

        if i < 5:
            input("\nPress Enter to continue...")
            clear_screen()

    print(f"\nGame Over! | Final score: {score}")
    return score


def yes_or_no(prompt):
    """Get a yes & return True or no to return False to play the game"""
    while True:
        resp = input(prompt).upper().strip()
        if resp in ['Y', 'YES']:
            return True
        elif resp in ['N', 'NO']:
            return False
        else:
            print("Invalid input! Try again.")

def main():
    """make the game repetitive, call other function and play game"""
    clear_screen()
    if not yes_or_no("Do you want to play the game? 'Yes' or 'No': "):
        print("Thank you and goodbye!")
        return

    while True:
        play_game()
        if not yes_or_no("Do you want to play again? 'Yes' or 'No': "):
            print("Thank you for playing and goodbye!")
            break
        clear_screen()

main()