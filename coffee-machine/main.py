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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))

def check_resources(drink_name):
    if drink_name == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            print("Please insert coins.")
        else:
            if resources["water"] < 50:
                print("Sorry there is not enough water.")
            elif resources["coffee"] < 18:
                print("Sorry there is not enough coffee.")
            return 0
    elif drink_name == "latte":
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            print("Please insert coins.")
        else:
            if resources["water"] < 200:
                print("Sorry there is not enough water.")
            elif resources["milk"] < 150:
                print("Sorry there is not enough milk.")
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee.")
            return 0
    elif drink_name == "cappuccino":
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            print("Please insert coins.")
        else:
            if resources["water"] < 250:
                print("Sorry there is not enough water.")
            elif resources["milk"] < 100:
                print("Sorry there is not enough milk.")
            elif resources["coffee"] < 24:
                print("Sorry there is not enough coffee.")
            return 0

def collect_money():
    q = float(input("how many quarters?: "))
    d = float(input("how many dimes?: "))
    n = float(input("how many nickles?: "))
    p = float(input("how many pennies?: "))
    return q, d, n, p

def process_coins(quarters,dimes,nickles,pennies):
    total_dollars = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total_dollars
def charge_amount(amount_received, charge, drink_name):
    if amount_received >= charge:
        change = round((amount_received - charge), 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        if drink_name == "espresso":
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
        elif drink_name == "latte":
            resources["water"] = resources["water"] - 200
            resources["milk"] = resources["milk"] - 150
            resources["coffee"] = resources["coffee"] - 24
        elif drink_name == "cappuccino":
            resources["water"] = resources["water"] - 250
            resources["milk"] = resources["milk"] - 100
            resources["coffee"] = resources["coffee"] - 24
        return charge
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

money = 0
machine_working = True

while machine_working != False:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        report()
    elif user_choice == "espresso":
        x = check_resources(user_choice)
        if x != 0:
            smthing = collect_money()
            coins = process_coins(quarters=float(smthing[0]), dimes=float(smthing[1]), nickles=float(smthing[2]),
                              pennies=float(smthing[3]))
            money += charge_amount(coins, 1.5,user_choice)
    elif user_choice == "latte":
        x = check_resources(user_choice)
        if x != 0:
            smthing = collect_money()
            coins = process_coins(quarters=float(smthing[0]), dimes=float(smthing[1]), nickles=float(smthing[2]),
                                  pennies=float(smthing[3]))
            money += charge_amount(coins, 2.5, user_choice)
    elif user_choice == "cappuccino":
        x = check_resources(user_choice)
        if x != 0:
            smthing = collect_money()
            coins = process_coins(quarters=float(smthing[0]), dimes=float(smthing[1]), nickles=float(smthing[2]),
                                  pennies=float(smthing[3]))
            money += charge_amount(coins, 3.0, user_choice)
    elif user_choice == "off":
        machine_working = False