#☕🐸

# TODO: 1. connect the coffee machine data with the python file - DONE

# TODO 2. create a prompt for user input - DONE

# TODO 3. create a get_report function to output: walk, milk, coffee and money in the machine - DONE

# TODO 4. create an if statement to check for off if the input from the user is 'off' - DONE

# TODO 5. create a sufficient_resources function to see if the machine has enough resources, it should return true - DONE

# TODO 6. create a function process_coins to calculate the payment

# TODO 7. create a function to return boolean value if the transaction is successful based on the payment received

# TODO 8. create a function to make coffee and deduct resources

import sys
sys.path.append("../Python_modules")
from coffee_machine_menu import MENU, resources

# print(MENU)
# print(resources)

profit = 0


def get_report(resources):
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${profit}\n"
          )


def sufficient_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(payment_received, drink_cost):
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("That's not enough money.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕🐸.")


def order_coffee():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            get_report(resources)
        elif choice == 'off':
            is_on = False
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            drink = MENU[choice]
            if sufficient_resources(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice, try again")


order_coffee()
