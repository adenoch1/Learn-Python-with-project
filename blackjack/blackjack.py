'''
Blackjack game

deal_card function
calculate_score function
compare_score function
play_game function
'''

import random, os, time

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Return the score. Return 0 to represent a 'blackjack' (2-card 21)."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    total = sum(cards)
    if total > 21 and 11 in cards:
        idx = cards.index(11)
        cards[idx] = 1
        total = sum(cards)

    return total

def compare_score(u_score, d_score):
    """Compare user and dealer's score and give the verdict of the game"""
    if u_score == d_score:
        return "It's a draw. Push!"
    elif d_score == 0:
        return "You lose! Dealer has blackjack."
    elif u_score == 0:
        return "You win! You have blackjack."
    elif d_score > 21:
        return "You win!"
    elif u_score > 21:
        return "You lose!"
    elif u_score > d_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """This will be called to play the game."""
    is_game_over = False
    user_cards = []
    dealer_cards = []

    # initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    # compute initial scores
    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    # reveal if either side has a blackjack and end the game
    if user_score == 0 or dealer_score == 0:
        print(f"Your card: {user_cards}, Dealer's card: {dealer_cards}")
        print(f"Your score: {user_score if user_score != 0 else 'Blackjack!'}, Dealer's score: {dealer_score if dealer_score != 0 else 'Blackjack!'}")
        if user_score == dealer_score:
            print("It's a draw. Push!")
        return

    # player turn to pick card
    while not is_game_over:
        user_score = calculate_score(user_cards)  # recalculate in case of A changes
        dealer_score = calculate_score(dealer_cards)

        print(f"User card: {user_cards}, User score: {user_score}")
        print(f"Dealer's card: {dealer_cards[0]}")

        if user_score > 21:
            is_game_over = True
            break

        choice = input("Do you want to pick a card? (y/n): ").lower().strip()
        if choice.startswith('y'):
            user_cards.append(deal_card())
        else:
            is_game_over = True

    # dealer's turn, if dealer is not a blackjack
    dealer_score = calculate_score(dealer_cards)
    if dealer_score != 0:
        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

    # final score
    user_score = calculate_score(user_cards)
    print("\nFinal hands:")
    print(f"Your card: {user_cards}, Your score: {user_score if user_score != 0 else 'Blackjack! You win.'}")
    print(f"Dealer's card: {dealer_cards}, Dealer's score: {dealer_score if dealer_score != 0 else 'Blackjack!. You lose.'}")
    print(compare_score(user_score, dealer_score))
    time.sleep(3)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    play = input("Type 'y' to play blackjack or 'n' to quit: ").lower().strip()
    if play == 'y':
        play_game()
    else:
        print("Thank you for playing! Goodbye!")
        break
