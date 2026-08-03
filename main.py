menu = {
    "espresso": {
        "ingredients": {"coffee_beans_g": 8, "water_ml": 30, "milk_ml": 0},
        "cost": 150.0,
    },
    "latte": {
        "ingredients": {"coffee_beans_g": 18, "water_ml": 50, "milk_ml": 150},
        "cost": 250.0,
    },
    "cappuccino": {
        "ingredients": {"coffee_beans_g": 18, "water_ml": 50, "milk_ml": 100},
        "cost": 300.0,
    },
}
resources = {
    "milk": 1000,
    "water": 2000,
    "coffee": 36,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    profit("please insert coins.")
    total = int(input("how many quarters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickels?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def is_transaction_succesful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved -  drink_cost , 2)
        print(f"here is ${change} in change .")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry there is not enough {item}.")

def make_coffee(drink_name , order_ingrediants):
    for item in order_ingrediants:
        resources[item] -= order_ingrediants[item]
    print(f"here is your {drink_name}")



profit = 0
report = "paisay !"
coffee_machine_on = True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['Milk']}ml")
        print(f"Coffee: {resources['Coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = menu["ingredients"]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment , drink["cost"]):
                make_coffee()
