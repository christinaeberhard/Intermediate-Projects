MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0.00
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_check(ingredients):
    """Returns True when order can be made or False if ingredients ar not enough."""
    is_enough = True
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough


def count_coins():
    """Returns the calculated total from all coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    print(f"You've given ${total}.")
    return total


def transaction_check(money_received, drink_costs):
    """Returns True when payment is accepted or False if money is insufficient."""
    if money_received >= drink_costs:
        change = round(money_received - drink_costs, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_costs
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, ingredients):
    """Substract the required ingredients from the resources."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕️")


machine_on = True

while machine_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino)\nOtherwise choose between 'report' and 'off': ")
    if choice == "off":
        machine_on = False
        print("Machine is off.")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resource_check(drink['ingredients']):
            payment = count_coins()
            if transaction_check(payment, drink['cost']):
                make_drink(choice, drink['ingredients'])

