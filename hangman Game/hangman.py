import random
from hangman_art import logo, hangman_images

lives = 6
word_list = ["pursue", "violet", "zebra", "excellent", "understanding", "peruse"]
chosen_word = random.choice(word_list)

blank_line = ['-' for _ in chosen_word]

print(logo)

guessed = set()

print("Welcome to hangman!")

while lives > 0 and '-' in blank_line:
    print(f"word: {''.join(blank_line)}")
    print(hangman_images[lives])
    print(f"You have {lives} lives | Guessed: {', '.join(sorted(guessed)) or 'none'}")

    guess = input("\nGuess a letter (a-z): ").lower().strip()
    if guess in guessed:
        print("You have already guessed that. Please try another letter.")
        continue

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    guessed.add(guess)

    if guess in chosen_word:
        for i, ch in enumerate(chosen_word):
            if ch == guess:
                blank_line[i] = guess
        print("Good guess!")
    else:
        print("Sorry, that was a wrong guess!")
        lives -= 1

# to end the game
print(f"Your guesses letters are: {', '.join(guessed)}")
print(f"You have {lives} lives left")
print(hangman_images[lives])

if '-' in blank_line:
    print("Sorry, you lost")
else:
    print("Congratulations! You won.")
    print("The word was:", chosen_word)
