MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
def check_resource(u_input,resource):
    global  MENU
    score = 0
    for keys in resources:
        if MENU[u_input]['ingredients'][keys] <= resource[keys] :
            score += 1

    if score == 3:
        return True
    else:
        return False

def coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total




off = False
while not off:

    user_input = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_input == 'off':
        off = True
        print('We are closed')

    elif user_input == 'report':
        print(resources)

    elif user_input in ["espresso","latte","cappuccino"]:
        check = check_resource(user_input,resources)
        if check:
            total_coins = coins()
            if total_coins >= MENU[user_input]['cost']:
                print(f"here is the change {total_coins-MENU[user_input]['cost']}")
                print(f'your {user_input} is ready. enjoy!')
                for i in resources:
                    resources[i] -= MENU[user_input]['ingredients'][i]


            else:
                print(f'here is your money {total_coins}')
        else:
            new = ""
            for i in resources:
                if MENU[user_input]['ingredients'][i] > resources[i]:
                    if len(new) ==0:
                        new = new + i
                    else:
                        new = new +", "+ i

            print(f'we dont have enough {new}')



