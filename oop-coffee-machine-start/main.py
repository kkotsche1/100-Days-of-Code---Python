from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Initializing individual drinks, machine, menu and payment objects

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

espresso = MenuItem(name = "espresso", water = 100, milk = 0, coffee = 18, cost = 1.50)

cappucino = MenuItem(name = "cappucino", water = 200, milk = 100, coffee = 24, cost = 3.00)

latte = MenuItem(name = "latte", water = 160, milk = 150, coffee = 22, cost = 2.50)

machine_on = True
while machine_on:
    user_round = True
    while user_round:
        drink_choice = input(f"The available items are {menu.get_items()} - Please enter which drink you would like.")

        if drink_choice == "espresso":
            if coffee_machine.is_resource_sufficient(espresso):
                money_machine.make_payment(espresso.cost)
                coffee_machine.make_coffee(espresso)
                user_round = False
            else:
                print(f"There are not enough resources in the coffee machine to make the coffee."
                      f"Currently available resources are {coffee_machine.report()}")
                user_round = False

        if drink_choice == "latte":
            if coffee_machine.is_resource_sufficient(latte):
                money_machine.make_payment(latte.cost)
                coffee_machine.make_coffee(latte)
                user_round = False
            else:
                print(f"There are not enough resources in the coffee machine to make the coffee."
                      f"Currently available resources are {coffee_machine.report()}")
                user_round = False

        if drink_choice == "cappucino":
            if coffee_machine.is_resource_sufficient(cappucino):
                money_machine.make_payment(cappucino.cost)
                coffee_machine.make_coffee(cappucino)
                user_round = False
            else:
                print(f"There are not enough resources in the coffee machine to make the coffee."
                      f"Currently available resources are {coffee_machine.report()}")
                user_round = False

        if drink_choice == "refill":
            print("Current Resources:")
            coffee_machine.report()
            coffee_machine.resources["water"] += 300
            coffee_machine.resources["coffee"] += 60
            coffee_machine.resources["milk"] += 300
            print("New resource levels")
            coffee_machine.report()


        if drink_choice == "report":
            coffee_machine.report()
            money_machine.report()