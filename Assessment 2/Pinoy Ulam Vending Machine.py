print("You only have ₱150 in your wallet, spend it well!")
rice = {
    1: {"name": "Plain Rice", "price": 15, "Stock": 21},
    2: {"name": "Garlic Rice", "price": 18, "Stock": 15},
    3: {"name": "Java Rice", "price": 18, "Stock": 15}
}
dish = {
    1: {"name": "Chicken Adobo", "price": 25, "Stock": 21},
    2: {"name": "Milkfish Sinigang", "price": 25, "Stock": 21},
    3: {"name": "Beef Kaldereta", "price": 25, "Stock": 21},
    4: {"name": "Lechon Paksiw", "price": 25, "Stock": 21},
    5: {"name": "Grilled Crocodile", "price": 30, "Stock": 21}
}
drinks = {
    1: {"name": "Cobra", "price": 16, "Stock": 30},
    2: {"name": "Sarsi", "price": 16, "Stock": 30},
    3: {"name": "RC", "price": 16, "Stock": 30},
    4: {"name": "Royal Orange", "price": 16, "Stock": 30}
}

total = 0
wallet = 150
tip_discount = 0
has_tipped = False  

def show_rice_menu():
    print("\nRice Menu:")
    for key, value in rice.items():
        print(f"{key}\t{value['name']} - Price: ₱{value['price']}")
    print("What type of rice would you like?")

def rice_choose():
    global total
    try:
        rice_choosing = int(input("- "))
        if rice_choosing in rice:
            selected = rice[rice_choosing]
            total += selected["price"]
            print(f"You chose: {selected['name']}.")
            show_dish_menu()
        else:
            print("That's not on the menu.")
            rice_choose()
    except ValueError:
        print("What's that?")
        rice_choose()

def show_dish_menu():
    print("\nDish Menu:")
    for key, value in dish.items():
        print(f"{key}\t{value['name']} - Price: ₱{value['price']}")
    print("What type of dish would you like to pair with your rice?")
    dish_choose()

def dish_choose():
    global total
    try:
        dish_choosing = int(input("- "))
        if dish_choosing in dish:
            selected = dish[dish_choosing]
            total += selected["price"]
            print(f"You chose: {selected['name']}.")
            show_drinks_menu()
        else:
            print("That's not on the menu.")
            dish_choose()
    except ValueError:
        print("What's that?")
        dish_choose()

def show_drinks_menu():
    print("\nDrinks Menu:")
    for key, value in drinks.items():
        print(f"{key}\t{value['name']} - Price: ₱{value['price']}")
    print("What drink would you like?")
    drink_choose()

def drink_choose():
    global total
    try:
        drink_choosing = int(input("- "))
        if drink_choosing in drinks:
            selected = drinks[drink_choosing]
            total += selected["price"]
            print(f"You chose: {selected['name']}.")
            print(f"\nYour total is: ₱{total - tip_discount}")
            ask_for_payment()
        else:
            print("That's not on the menu.")
            drink_choose()
    except ValueError:
        print("What's that?")
        drink_choose()

def ask_for_payment():
    global total, wallet, tip_discount
    try:
        if tip_discount > 0:
            print(f"A ₱{tip_discount} discount has been applied to your total.")
            total -= tip_discount
            tip_discount = 0

        if wallet < total:
            print(f"You only have ₱{wallet} left in your wallet and the total price is ₱{total}.")
            print("You don't have enough money.")
            retry = input("Do you want to pay the proper amount or cancel your order? type 'pay' if yes and 'cancel' if no: ").strip().lower()
            if retry == "pay":
                ask_for_payment()
            elif retry == "cancel":
                print("You cancelled your order. Thank you!")
            else:
                print("What's that? The only options are 'pay' and 'cancel'.")
                ask_for_payment()
        else:
            amount = float(input(f"Enter your payment (You only have ₱{wallet} left): ₱"))
            if amount > wallet:
                print("You don't have that amount of money.")
                ask_for_payment()
            elif amount < total:
                print(f"Your money is not enough. The total price is ₱{total}.")
                retry = input("Do you want to pay the proper amount or cancel your order? type 'pay' if yes and 'cancel' if no: ").strip().lower()
                if retry == "pay":
                    ask_for_payment()
                elif retry == "cancel":
                    print("You cancelled your order. Thank you!")
                else:
                    print("What's that? The only options are 'pay' and 'cancel'.")
                    ask_for_payment()
            else:
                change = amount - total
                wallet -= total
                print(f"Thank you! You have paid ₱{amount:.2f}. Your change is ₱{change:.2f}.")
                print(f"You only have ₱{wallet} left.")
                ask_for_tip()
    except ValueError:
        print("What's that?")
        ask_for_payment()

def ask_for_tip():
    global tip_discount, wallet, total, has_tipped
    if has_tipped:
        print("You've already left a tip. Thank you again!")
        ask_for_more_purchase()
        return

    tip_choice = input("\nWould you like to leave a tip? This is optional: ").strip().lower()
    if tip_choice == "yes":
        while True:
            try:
                tip = float(input("Enter the amount you want to tip: ₱"))
                if tip > 0:
                    if wallet >= tip:
                        tip_discount = 10
                        wallet -= tip
                        total += tip
                        has_tipped = True
                        print(f"Thank you for your tip of ₱{tip:.2f}! You now only have ₱{wallet} left.")
                        break
                    else:
                        print("You don't have enough money.")
                else:
                    print("Please enter a valid tip amount.")
            except ValueError:
                print("I don't think that's money.")
    elif tip_choice == "no":
        print("No problem! Thank you for your purchase.")
    else:
        print("Please answer 'yes' or 'no'.")
    ask_for_more_purchase()

def ask_for_more_purchase():
    global total, tip_discount, wallet
    more_purchase = input("\nWould you like to make another purchase? yes or no?: ").strip().lower()
    if more_purchase == "yes":
        total = 0
        show_rice_menu()
        rice_choose()
    elif more_purchase == "no":
        print(f"Thank you for your purchase! You now only have ₱{wallet} in your wallet.")
    else:
        print("Please answer 'yes' or 'no'.")
        ask_for_more_purchase()

show_rice_menu()
rice_choose()