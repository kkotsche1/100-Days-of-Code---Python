# Coffee machine script
machine_on = True

while machine_on:


    total_collected = 0
    water = 0
    coffee = 0
    milk = 0


    def fill_machine():
        global water
        global milk
        global coffee
        print(f"The current fill Status is"
              f"Water = {water}"
              f"Milk = {milk}"
              f"coffee = {coffee}")
        water += 300
        milk += 200
        coffee += 100
        print (f"The machine has been succesfully refilled! New status:"
               f"Water = {water}"
               f"Milk = {milk}"
               f"coffee = {coffee}")


    def make_espresso():
        global water
        global coffee
        water -= 50
        coffee -= 18

    def make_latte():
        global water
        global coffee
        global milk
        water -= 200
        coffee -=24
        milk -=150

    def make_cappucino():
        global water
        global coffee
        global milk
        water -= 250
        coffee -= 24
        milk -= 100

    def drink_payment(user_choice):
        global total_collected
        cost = 0
        if user_choice == "E":
            cost = 150
        if user_choice == "L":
            cost = 250
        if user_choice == "C":
            cost = 300
        user_paid = 0
        print(f"Your chosen Beverage costs {cost/100} dollars, please pay accordingly. "
              f"Enter P for penny, N for Nickel, D for dime, or Q for Quarter ")
        while user_paid < cost:
            print(f"Your current total amount paid is: {user_paid/100}$\n")
            user_coin = input("Please enter a coin\n")
            if user_coin == "P":
                user_paid += 1
                total_collected += 1
            if user_coin == "N":
                user_paid += 5
                total_collected += 5
            if user_coin == "D":
                user_paid += 10
                total_collected += 10
            if user_coin == "Q":
                user_paid += 25
                total_collected += 25

        print(f"Your total amount paid is {user_paid}")
        if user_paid > cost:
            print(f"You paid too much! You will receive change in the amount of {(user_paid - cost)/100}$")
        if user_paid >= cost:
            return True

    def print_report():
        global total_collected
        global water
        global coffee
        global milk
        print(f"The total amount of money collected is: {total_collected/100}$")
        print(f"The total amount of milk left is: {milk}")
        print(f"The total amount of water left is: {water}")
        print(f"The total amount of coffee left is: {coffee}")


    user_entry = True
    while user_entry:
        user_choice = input("Welcome to the coffee machine, what drink would you like?"
                             "Enter E for Espresso, L for Latte and C for Cappucino")

        if user_choice == "E":
            succesful_payment = drink_payment(user_choice)
            if succesful_payment:
                if water >= 50 and coffee >= 18:
                    make_espresso()
                    print("Here is your Espresso! :)")

                elif water < 50:
                    print("There is not enough Water in the coffee machine."
                          "You will be refunded: $1.50")

                elif coffee < 18:
                    print("There is not enough Coffee in the coffee machine."
                          "You will be refunded: $1.50")

            else:
                print ("You did not pay!")
                user_entry = False

        if user_choice == "L":
            succesful_payment = drink_payment(user_choice)
            if succesful_payment:
                if water >= 200 and coffee >= 24 and milk > 150:
                    make_latte()
                    print("Here is your Latte! :)")

                elif water < 200:
                    print (water)
                    print("There is not enough Water in the coffee machine."
                          "You will be refunded: $2.50")

                elif coffee < 24:
                    print("There is not enough Coffee in the coffee machine."
                          "You will be refunded: $2.50")

                elif milk < 150:
                    print("There is not enough Milk in the coffee machine."
                          "You will be refunded: $2.50")

            else:
                print("You did not pay!")
                user_entry = False

        if user_choice == "C":
            succesful_payment = drink_payment(user_choice)
            if succesful_payment:
                if water >= 250 and coffee >= 24 and milk >= 100:
                    make_cappucino()
                    print("Here is your Cappucino! :)")

                elif water < 250:
                    print("There is not enough Water in the coffee machine."
                          "You will be refunded: $2.50")

                elif coffee < 24:
                    print("There is not enough Coffee in the coffee machine."
                          "You will be refunded: $2.50")

                elif milk < 100:
                    print("There is not enough Milk in the coffee machine."
                          "You will be refunded: $2.50")

            else:
                print ("You did not pay!")
                user_entry = False

        if user_choice == "report":
            print_report()


        if user_choice == "off":
            machine_on = False

        if user_choice == "refill":
            fill_machine()
