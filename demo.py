import time

# --- Global Data ---
prices = {"Espresso": 1.50, "Latte": 2.50, "Capuccino": 3.00}
available_resources = {"water": 300, "milk": 200, "coffee": 100, "coin": 0}

requirement = {
    "espresso": {"water": 50, "coffee": 18},
    "latte": {"water": 200, "coffee": 24, "milk": 150},
    "capuccino": {"water": 250, "coffee": 24, "milk": 100}
}

# --- Utility Functions ---
def report(resources):
    print("\n📊 Current Machine Resources:")
    for key, value in resources.items():
        print(f"  {key.capitalize()}: {value}")
    print()

def get_choice(valid_choices, prompt):
    while True:
        choice = input(prompt).lower().strip()
        if choice in valid_choices:
            return choice
        print("Invalid input. Try again.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")

# --- Core Coffee Logic ---
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
        return True
    else:
        print("\n❌ Sorry, not enough resources to make this order.")
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

def get_payment(cost):
    """Handle payment and return True if successful."""
    print(f"\n💵 Your total is ${cost:.2f}")
    quarters = get_int("How many quarters? ")
    dimes = get_int("How many dimes? ")
    nickels = get_int("How many nickels? ")
    pennies = get_int("How many pennies? ")

    total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    if total_paid < cost:
        print(f"❌ Not enough money. Refunding ${total_paid:.2f}.\n")
        return False
    else:
        change = round(total_paid - cost, 2)
        available_resources["coin"] += cost
        print(f"✅ Payment accepted. Your change is ${change:.2f}.")
        return True

def make_coffee():
    """Simulate the coffee-making process."""
    print("\n☕ Making your coffee...")
    time.sleep(2)
    print("✅ Coffee ready! Enjoy your drink!\n")

def refill_machine(resources):
    """Refill resources by the barista/admin."""
    print("\n🧑‍🔧 Refilling machine...")
    time.sleep(1)
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    print("✅ Machine refilled successfully!\n")

# --- Main Program Loop ---
def coffee_machine():
    print("Welcome to the Python Coffee Machine! ☕")
    print("---------------------------------------")

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
                if check_resources(requirement, order, available_resources):
                    if get_payment(total_cost):
                        make_coffee()
                else:
                    print("Please wait for the barista to refill the machine.")
            else:
                print("Order cancelled.\n")

        elif action == "report":
            report(available_resources)

        elif action == "refill":
            # In a real-world scenario, only staff can refill
            admin_key = input("Enter admin password to refill: ").strip()
            if admin_key == "admin123":  # Simple demo password
                refill_machine(available_resources)
            else:
                print("❌ Incorrect password. Access denied.\n")

        elif action == "quit":
            print("\n👋 Shutting down coffee machine. Have a great day!")
            break

# Run the machine
coffee_machine()
