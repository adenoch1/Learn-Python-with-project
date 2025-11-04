""" number guessing game"""

import random, time, os

def number_guessing_game():
    """to play the number guessing game"""
    live = 0
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100...")
    number = random.randint(1, 100)

    # choose a level between hard and easy
    while True:
        level = input("Type 'hard' to chose hard level or 'easy' to chose easy level: ").lower().strip()
        if level == 'hard':
            live = 5
            break
        elif level == 'easy':
            live = 10
            break
        else:
            print("Invalid input. Please try again.")

    # to guess the number
    while live > 0:
        print(f"\nYou have {live} attempt left.")
        guess = input("Guess a number between 1 and 100: ")

        try:
            choice = int(guess)
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        # check if in range
        if not 1 <= choice <= 100:
            print("Choose a number between 1 and 100.")
            continue

        if choice > number:
            print("Too high.")
            live -= 1
        elif choice < number:
            print("Too low.")
            live -= 1
        else:
            print("Correct guess!")
            print("The number was indeed", number)
            time.sleep(1)
            return

    print("\nSorry, you have run of live.")
    print("The number was indeed", number)
    time.sleep(2)

def clear_screen():
    """to clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_screen()
    interest = input("Will you like to play a number guessing game? (y/n): ").lower().strip()
    if interest in ['y', 'yes']:
        number_guessing_game()
    elif interest in ['n', 'no']:
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")