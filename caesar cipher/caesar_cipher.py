# caesar cipher encryption

import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

def caesar(text: str, shift_number: int, mode: str):
    if mode == "decode":
        shift_number = -shift_number

    result = []

    for char in text:
        if char in lower:
            new_position = lower.index(char)
            final_position = (new_position + shift_number) % len(lower)
            result.append(lower[final_position])
        elif char in upper:
            new_position = upper.index(char)
            final_position = (new_position + shift_number) % len(upper)
            result.append(upper[final_position])
        elif char in digits:
            new_position = digits.index(char)
            final_position = (new_position + shift_number) % len(digits)
            result.append(digits[final_position])
        elif char in symbols:
            new_position = symbols.index(char)
            final_position = (new_position + shift_number) % len(symbols)
            result.append(symbols[final_position])
        else:
            result.append(char)

    print(f"The {mode}d text is: {''.join(result)}")

while True:
    while True:
        mode = input("Type 'encode' to encrypt or 'decode' to decrypt: ").strip()
        if mode == "encode" or mode == "decode":
            break
        else:
            print("Invalid input.")

    text = input("Type the text to encrypte or decrypt: ")

    while True:
        shift_number = input("Type the shift number: ")
        try:
            shift_number = int(shift_number)
            break
        except ValueError:
            print("Type a number pls. ")

    caesar(text, shift_number, mode)

    restart = input("Type 'yes' to restart or 'no' to end: ").lower().strip()
    if restart == "yes":
        print("The program is restarting.")
    else:
        print("Goodbye.")
        break

