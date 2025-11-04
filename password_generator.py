
import string
import random


letters = string.ascii_letters
digits = string.digits
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print(letters)


number_of_letters = int(input("How many letters do you want in your password?\n"))
number_of_digits = int(input("How many digits do you want in your password?\n"))
number_of_symbols = int(input("How many symbols do you want in your password?\n"))

choice_letters = random.choices(letters, k=number_of_letters)
choice_digits = random.choices(digits, k=number_of_digits)
choice_symbols = random.choices(symbols, k=number_of_symbols)

choice_password = choice_letters + choice_digits + choice_symbols
random.shuffle(choice_password)
password = "".join(choice_password)

print(f"Your password is {password}")