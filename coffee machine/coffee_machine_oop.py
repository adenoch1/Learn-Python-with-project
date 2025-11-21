import time, os, json

class CoffeeMachine:
    STATE_FILE = "machine_state.json"   # class attribute

    def __init__(self):
        # --- Global Data ---   instance attributes
        self.prices = {"Espresso": 1.50, "Latte": 2.50, "Capuccino": 3.00}
        self.default_resources = {"water": 300, "milk": 200, "coffee": 100, "coin": 0.0}
        self.requirement = {
            "espresso": {"water": 50, "coffee": 18},
            "latte": {"water": 200, "coffee": 24, "milk": 150},
            "capuccino": {"water": 250, "coffee": 24, "milk": 100}
        }
        self.resources = self.load_state()

   # methods
    # --- Persistence Functions ---
    def load_state(self):
        """Load machine state from JSON file if it exists, else use defaults."""
        if os.path.exists(self.STATE_FILE):
            try:
                with open(self.STATE_FILE, "r") as f:
                    data = json.load(f)
                    print("Machine state loaded successfully.\n")
                    return data
            except (json.JSONDecodeError, IOError):
                print("State file corrupted. Resetting to default resources.\n")
                return self.default_resources.copy()
        else:
            print("No saved state found. Using default resources.\n")
            self.save_state()
            return self.default_resources.copy()

    def save_state(self):
        """Save current machine state to file."""
        try:
            with open(self.STATE_FILE, "w") as f:
                json.dump(self.resources, f, indent=4)
        except IOError:
            print("Could not save machine state!")


    # --- Utility Functions ---
    def report(self):
        """to give report about available resources"""
        print("\nCurrent Machine Resources:")
        for key, value in self.resources.items():
            if key == "water" or key == "milk":
                print(f"  {key.capitalize()}: {value}ml")
            elif key == "coffee":
                print(f"  {key.capitalize()}: {value}g")
            else:
                print(f"  {key.capitalize()}: ${value}")
        print()

    def get_choice(self, valid_choices, prompt):
        """to get correct input from user and return their choice"""
        while True:
            choice = input(prompt).lower().strip()
            if choice in valid_choices:
                return choice
            print("Invalid input. Try again.")

    def get_int(self, prompt):
        """to ensure we are getting integer input from user"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Enter a number.")


    def check_resources(self, order):
        """Return True if enough ingredients, else False."""
        total_water = total_coffee = total_milk = 0

        for drink, qty in order.items():
            for resource, amount in self.requirement[drink].items():
                if resource == "water":
                    total_water += amount * qty
                elif resource == "coffee":
                    total_coffee += amount * qty
                elif resource == "milk":
                    total_milk += amount * qty

        if (self.resources["water"] >= total_water and
            self.resources["coffee"] >= total_coffee and
            self.resources["milk"] >= total_milk):
            self.resources["water"] -= total_water
            self.resources["coffee"] -= total_coffee
            self.resources["milk"] -= total_milk
            self.save_state()
            return True
        else:
            print("\nSorry, not enough resources to make this order.")
            return False

    def get_order(self, flavors):
        """Take order(s) from the customer."""
        order = {"espresso": 0, "latte": 0, "capuccino": 0}
        while True:
            drink = self.get_choice(flavors, "What would you like? (espresso/latte/capuccino): ")
            qty = self.get_int(f"How many {drink} would you like? ")
            order[drink] += qty
            more = self.get_choice(["yes", "no"], "Would you like to order more? (yes/no): ")
            if more == "no":
                break
        return order

    def calculate_total(self, order):
        """Compute total cost for the given order."""
        return sum(self.prices[k.capitalize()] * v for k, v in order.items())

    def get_payment(self, cost):
        """Handle payment and return True if successful."""
        print(f"\nYour total is ${cost:.2f}")
        quarters = self.get_int("How many quarters? ")
        dimes = self.get_int("How many dimes? ")
        nickels = self.get_int("How many nickels? ")
        pennies = self.get_int("How many pennies? ")

        total_paid = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
        if total_paid < cost:
            print(f"Not enough money. Refunding ${total_paid:.2f}.\n")
            return False
        else:
            change = round(total_paid - cost, 2)
            self.resources["coin"] += cost
            self.save_state()
            print(f"Payment accepted. Your change is ${change:.2f}.")
            return True


    def make_coffee(self):
        """Simulate the coffee-making process."""
        print("\n☕ Making your coffee...")
        time.sleep(2)
        print("Coffee ready! Enjoy your drink!\n")

    def refill_machine(self):
        """Refill resources by the barista/admin."""
        print("\nRefilling machine...")
        time.sleep(1)
        self.resources["water"] = 300
        self.resources["milk"] = 200
        self.resources["coffee"] = 100
        self.save_state()
        print("Machine refilled successfully!\n")


    def run(self):
        """make the coffee machine repetitive"""
        print("Welcome to the Python Coffee Machine! ☕")
        print("---------------------------------------")


        while True:
            action = self.get_choice(
                ["coffee", "report", "refill", "quit"],
                "\nType 'coffee' to order, 'report' for resources, 'refill' (admin), or 'quit' to exit: "
            )

            if action == "coffee":
                order = self.get_order(["espresso", "latte", "capuccino"])
                total_cost = self.calculate_total(order)
                print("\nYour final order:")
                for k, v in order.items():
                    print(f"  {k.capitalize()}: {v}")
                print(f"Total cost: ${total_cost:.2f}")

                confirm = self.get_choice(["yes", "no"], "Confirm your order? (yes/no): ")
                if confirm == "yes":
                    if self.check_resources(order):
                        if self.get_payment(total_cost):
                            self.make_coffee()
                    else:
                        print("Please wait for the barista to refill the machine.")
                else:
                    print("Order cancelled.\n")

            elif action == "report":
                self.report()

            elif action == "refill":
                admin_key = input("Enter admin password to refill: ").strip()
                if admin_key == "admin123":  # Simple demo password
                    self.refill_machine()
                else:
                    print("Incorrect password. Access denied.\n")

            elif action == "quit":
                print("\nSaving machine state...")
                self.save_state()
                print("Shutting down coffee machine. Have a great day!")
                break

# Run the machine
machine = CoffeeMachine()
machine.run()