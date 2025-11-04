# calculator
import time
import os


def get_float(prompt):
    """This is to check the validity of the input as a float"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def calculator():
    """This is to perform the calculations"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to your calculator!")

    first_number = get_float("Enter the first number: ")

    while True:
        lst_operation = ['+', '-', '*', '/']
        for char in lst_operation:
            print(char)
        operation = input("Pick an operation: ").strip()
        second_number = get_float("Enter the second number: ")

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        elif operation == "/":
            if second_number != 0:
                result = first_number / second_number
            else:
                print("Please enter a number.")
                continue
        else:
            print("Invalid operation. Try again.")
            continue

        print(f"{first_number} {operation} {second_number} = {result}")


        restart = input(f"Type 'y' to continue the calculation with {result}, 'n' to start a new calculation or 'q' to quit: ")
        if restart == "y":
            first_number = result
            continue
        elif restart == "n":
            calculator()
            break
        elif restart == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Exiting!")
            break

calculator()