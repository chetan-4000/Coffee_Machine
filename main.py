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

return_money = 0
profit = 0
is_on = True
while is_on:
    Input = input("What would you like?(espresso/latte/cappuccino):\n").lower()
    if Input == "report":
        print(resources['water'])
        print(resources['milk'])
        print(resources['coffee'])
        print(profit)

    elif Input == "off":
        is_on = False

    elif Input == "espresso" :
        money = float(input("Enter The Amount of Money:\n"))
        if resources['water'] >= 50 and resources['coffee'] >= 18:
            if money >= 1.5:
                return_money = money - 1.5
                resources['water'] -= 50
                resources['coffee'] -= 18
                profit = profit + 1.5
                print(f"Returned Money is {return_money}")
                print("Enjoy Your Coffee!")
            else:
                 print("Not enough Money")
        else:
             is_on = False
             print("Not Enough Resourses!")

    elif Input == "latte":
        money = float(input("Enter The Amount of Money:\n"))
        if resources['water'] >= 200 and resources['coffee'] >= 24 and resources['milk'] >= 150:
            if money >= 2.5:
                return_money = money - 2.5
                resources['water'] -= 200
                resources['coffee'] -= 24
                resources['milk'] -= 150
                profit = profit + 2.5
                print(f"Returned Money is {return_money}")
                print("Enjoy Your Coffee!")
            else:
                 print("Not enough Money")
        else:
             is_on = False
             print("Not Enough Resourses!")

    elif Input == "cappuccino":
        money = float(input("Enter The Amount of Money:\n"))
        if resources['water'] >= 250 and resources['coffee'] >= 24 and resources['milk'] >= 100:

            if money >= 3.0:
                return_money = money - 3.0
                resources['water'] -= 250
                resources['coffee'] -= 24
                resources['milk'] -= 100
                profit = profit + 3.0
                print(f"Returned Money is {return_money}")
                print("Enjoy Your Coffee!")
            else:
                 print("Not enough Money")
        else:
             is_on = False
             print("Not Enough Resourses!")