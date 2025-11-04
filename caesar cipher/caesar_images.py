"""
Step 1: Understand the Problem
What is Caesar Cipher?
It’s a simple encryption technique where each letter in a message is shifted by a fixed number in the alphabet.
Example: with a shift of 3, A → D, B → E, …, X → A, Y → B, Z → C.

Step 2: Break the Project into Subproblems
Instead of writing one big code block, we divide it into small tasks:
Any input: encode or decode, text, shift number def encrypt(text, shift_number, mode).   def decrypt(text, shift_number, mode)

What output is expected: final encryption or decrytion value. result = [] or ""

lowercase alphabet, upper alphabets, digits, symbols . string module
You need a value that will accept the final value (string or list)

Loop through each character in the text.
Check if the character is a letter, digits, punctuation.
Shift the letter by the shift number:
Convert letter → number (ASCII value or alphabet index).
Apply the shift.
Wrap around if it goes past Z. a- z % (26)
Convert back to a letter, symbols, digits.
Build the encrypted string step by step.

Two functions: encrypt & decrypt.
Can the two functions be written as one function (DRY).

Can the encryption restart till the user tell it to end.
"""