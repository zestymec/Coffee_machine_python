menu = {
    "espresso": {
        "ingredients": {"coffee": 8, "water": 30, "milk": 0},
        "cost": 1,
    },
    "latte": {
        "ingredients": {"coffee": 18, "water": 50, "milk": 15},
        "cost": 2,
    },
    "cappuccino": {
        "ingredients": {"coffee": 18, "water": 50, "milk": 10},
        "cost": 3,
    },
}

resources = {
    "milk": 1000,
    "water": 2000,
    "coffee": 36,
}

profit = 0
coffee_machine_on = True


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice in menu:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")  