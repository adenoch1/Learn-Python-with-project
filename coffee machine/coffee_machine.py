"""
coffee machine project with persistent data
import time, os, json
Write your global data
define state file for persistent variable
Write two functions to load a python dictionary from a json file  and to save a json file from a python file
Write the following functions:
report() - to give information about available resources
get_choice() - to ensure the correct choice everytime we are using an input function
get_int() - to ensure the input is an integer
check_resources() - to check if there are enough resources for each order
get_order() - to get user's order
calculate_total_cost() - to calculate the total cost of each order
get_payment() - to get payment
make_coffee() - to make a coffee
refill_machine() - to refill the coffee machine with water, milk and coffee
coffee_machine() - main function to make the coffee machine repetitive
"""

import time, os, json

# --- Global Data ---
prices = {"Espresso": 1.50, "Latte": 2.50, "Capuccino": 3.00}
default_resources = {"water": 300, "milk": 200, "coffee": 100, "coin": 0.0}
requirement = {
    "espresso": {"water": 50, "coffee": 18},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "capuccino": {"water": 250, "coffee": 24, "milk": 100}
}

STATE_FILE = "machine_state.json"

# --- Persistence Functions ---
def load_state():
    """Load machine state from JSON file if it exists, else use defaults."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r") as f:
                data = json.load(f)
                print("Machine state loaded successfully.\n")
                return data
        except (json.JSONDecodeError, IOError):
            print("State file corrupted. Resetting to default resources.\n")
            return default_resources.copy()
    else:
        print("No saved state found. Using default resources.\n")
        save_state(default_resources)
        return default_resources.copy()

def save_state(resources):
    """Save current machine state to file."""
    try:
        with open(STATE_FILE, "w") as f:
            json.dump(resources, f, indent=4)
    except IOError:
        print("Could not save machine state!")


# --- Utility Functions ---
def report(resources):
    """to give report about available resources"""
    print("\nCurrent Machine Resources:")
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f"  {key.capitalize()}: {value}ml")
        elif key == "coffee":
            print(f"  {key.capitalize()}: {value}g")
        else:
            print(f"  {key.capitalize()}: ${value}")
    print()

def get_choice(valid_choices, prompt):
    """to get correct input from user and return their choice"""
    while True:
        choice = input(prompt).lower().strip()
        if choice in valid_choices:
            return choice
        print("Invalid input. Try again.")

def get_int(prompt):
    """to ensure we are getting integer input from user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")


def check_resources(requirement, order, resources):
    """Return True if enough ingredients, else False."""
    total_water = total_coffee = total_milk = 0

    for drink, qty in order.items():
        for resource, amount in requirement[drink].items():
            if resource == "water":
                total_water += amount * qty
            elif resource == "coffee":
                total_coffee += amount * qty
            elif resource == "milk":
                total_milk += amount * qty

    if (resources["water"] >= total_water and
        resources["coffee"] >= total_coffee and
        resources["milk"] >= total_milk):
        resources["water"] -= total_water
        resources["coffee"] -= total_coffee
        resources["milk"] -= total_milk
        save_state(resources)
        return True
    else:
        print("\nSorry, not enough resources to make this order.")
        return False

def get_order(flavors):
    """Take order(s) from the customer."""
    order = {"espresso": 0, "latte": 0, "capuccino": 0}
    while True:
        drink = get_choice(flavors, "What would you like? (espresso/latte/capuccino): ")
        qty = get_int(f"How many {drink} would you like? ")
        order[drink] += qty
        more = get_choice(["yes", "no"], "Would you like to order more? (yes/no): ")
        if more == "no":
            break
    return order

def calculate_total(order):
    """Compute total cost for the given order."""
    return sum(prices[k.capitalize()] * v for k, v in order.items())

def get_payment(cost, resources):
    """Handle payment and return True if successful."""
    print(f"\nYour total is ${cost:.2f}")
    quarters = get_int("How many quarters? ")
    dimes = get_int("How many dimes? ")
    nickels = get_int("How many nickels? ")
    pennies = get_int("How many pennies? ")

    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total_paid < cost:
        print(f"Not enough money. Refunding ${total_paid:.2f}.\n")
        return False
    else:
        change = round(total_paid - cost, 2)
        resources["coin"] += cost
        save_state(resources)
        print(f"Payment accepted. Your change is ${change:.2f}.")
        return True


def make_coffee():
    """Simulate the coffee-making process."""
    print("\n☕ Making your coffee...")
    time.sleep(2)
    print("Coffee ready! Enjoy your drink!\n")

def refill_machine(resources):
    """Refill resources by the barista/admin."""
    print("\nRefilling machine...")
    time.sleep(1)
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    save_state(resources)
    print("Machine refilled successfully!\n")


def coffee_machine():
    """make the coffee machine repetitive"""
    print("Welcome to the Python Coffee Machine! ☕")
    print("---------------------------------------")

    resources = load_state()

    while True:
        action = get_choice(
            ["coffee", "report", "refill", "quit"],
            "\nType 'coffee' to order, 'report' for resources, 'refill' (admin), or 'quit' to exit: "
        )

        if action == "coffee":
            order = get_order(["espresso", "latte", "capuccino"])
            total_cost = calculate_total(order)
            print("\nYour final order:")
            for k, v in order.items():
                print(f"  {k.capitalize()}: {v}")
            print(f"Total cost: ${total_cost:.2f}")

            confirm = get_choice(["yes", "no"], "Confirm your order? (yes/no): ")
            if confirm == "yes":
                if check_resources(requirement, order, resources):
                    if get_payment(total_cost, resources):
                        make_coffee()
                else:
                    print("Please wait for the barista to refill the machine.")
            else:
                print("Order cancelled.\n")

        elif action == "report":
            report(resources)

        elif action == "refill":
            admin_key = input("Enter admin password to refill: ").strip()
            if admin_key == "admin123":  # Simple demo password
                refill_machine(resources)
            else:
                print("Incorrect password. Access denied.\n")

        elif action == "quit":
            print("\nSaving machine state...")
            save_state(resources)
            print("Shutting down coffee machine. Have a great day!")
            break

# Run the machine
coffee_machine()