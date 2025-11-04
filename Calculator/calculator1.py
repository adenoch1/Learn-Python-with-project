"""Another version of calculator code"""

def add(n1, n2):
    """This is to add two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """This is to subtract two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """This is to multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """This is to divide two numbers"""
    global second_number
    while True:
        if n2 != 0:
            return n1 / n2
        else:
            print("You cannot divide by zero")
            n2 = int(input("Enter the number to divide: "))


def get_float(prompt):
    """This is to get a floating point number"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")

def calculator():
    print("Welcome to the calculator!")
    first_number = get_float("Enter the first number: ")

    while True:
        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }

        for operation in operations:
            print(operation)
        choice = input("Pick an operation: ")
        second_number = get_float("Enter the second number: ")

        if choice in operations:
            result = operations[choice](first_number, second_number)
        else:
            print("Invalid choice")
            continue

        print(f"{first_number} {choice} {second_number} = {result}")

        restart = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation or 'q' to quit: ")
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
            print("Invalid input! Exiting...")
            break


calculator()
