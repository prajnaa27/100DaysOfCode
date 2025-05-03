
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

def calculate_total_money(q,d,n,p):
    total=0.25*q+0.1*d+0.05*n+0.01*p
    return total

def check_resources(coffe_type):
    ingredients=MENU[coffe_type]['ingredients']
    cost=MENU[coffe_type]['cost']
    # print(ingredients)
    # print(cost)
    # print(resources)
    for ingredient in ingredients:
        # print(ingredient)
        quantity=ingredients[ingredient]
        if resources[ingredient]>=quantity:
            # print("true")
            continue
        else:
            print(f"Sorry there is not enough {ingredient}")
            return False
        # return True
    return True
        # print(quantity)

def update_resources(coffee_t,total):
    print(f"total {total}")
    for key in resources:
        if key=='money':
            resources['money']=resources['money']+total
        else:
            if key in MENU[coffee_t]['ingredients']:
                resources[key]=resources[key]-MENU[coffee_t]['ingredients'][key]
            else:
                continue

def print_report():
    measurements={'water':'ml','milk':'ml','coffee':'g','money':'$'}
    for key in resources:
        if key in measurements:
            suffix=measurements[key]
            # print(suffix)
        print(f"{key.title()}:{resources[key]}{suffix}")
    # print(resources)

resources['money']=0
def make_coffee():
    action_completed = True
    while action_completed:
        coffee_type=input("What would you like? (espresso/latte/cappuccino):").lower()
        global resources
        if coffee_type=='off':
            action_completed=True
            exit(0)
        if coffee_type=='report':
            print_report()
        if coffee_type=='espresso' or coffee_type=='latte' or coffee_type=='cappuccino':
            is_resource=check_resources(coffee_type)
            if is_resource:
                print("Please insert coins.")
                quarters=int(input("How many quarters?"))
                dimes=int(input("How many dimes?"))
                nickels=int(input("How many nickels?"))
                pennies=int(input("How many pennies?"))
                total=calculate_total_money(quarters,dimes,nickels,pennies)
                # print(total)
                cost=MENU[coffee_type]['cost']
                # print(f"cost:{cost}")
                if cost>total:
                    print("Not enough money")
                else:
                    update_resources(coffee_type,cost)
                    print(resources)
                    change=round(total-cost,2)
                    print(f"Here's ${change} in change")
                    print(f"Here's your {coffee_type}, Please enjoy!")



make_coffee()
