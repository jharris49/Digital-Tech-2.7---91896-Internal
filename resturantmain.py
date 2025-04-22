"""This file is a restaurants till operating system.

It lets the user create, edit, and cancel customer
orders for the restaurant.
"""
import inputvalidation
import time
import os
import sys
import random

# Stores the restarant menu (meal, price).
RESTAURANT_MENU = [
    ("Beef Burger", 16.99),
    ("Chicken Burger", 15.99),
    ("Fish Burger", 17.99),
    ("Vege Burger", 16.99),
    ("Sirloin Steak", 31.99),
    ("Margarita Pizza", 18.99),
    ("Pepperoni Pizza", 18.99),
    ("Vegetarian Pizza", 20.99),
    ]

# Stores customer order.
order = [

]

# Stores restaurants service charge perecentage.
SERVICE_CHARGE_PERC = 0.05


# Dictionary containing the meals
# and their corrosponding ingredients.
MEAL_CONTENTS = {
    "Beef Burger":
        ["Ground beef patty",
            "Cheese",
            "Tomato",
            "Lettuce",
            "Brioche bun",
            "Onion",
            "Oakwood burger sauce"],
    "Chicken Burger":
        ["Chicken breast",
            "Cheese",
            "Tomato",
            "Lettuce",
            "Brioche Bun",
            "Oakwood burger sauce"],
    "Fish Burger":
        ["Battered cod",
            "Cheese",
            "Tomato",
            "Lettuce",
            "Brioche bun",
            "Oakwood burger sauce"],
    "Vege Burger":
        ["Bean patty",
            "Cheese",
            "Tomato",
            "Lettuce",
            "Coleslaw",
            "Brioche bun",
            "Oakwood burger sauce"],
    "Sirloin Steak":
        ["250g sirloin steak",
            "Mashed potatoes",
            "Roasted vegetables",
            "Garlic butter"],
    "Margherita Pizza":
        ["Pizza sauce",
            "Cheese",
            "Fresh basil",
            "Fresh tomatoes"],
    "Pepperoni Pizza":
        ["Pizza sauce",
            "Cheese",
            "Pepporoni"],
    "Vegetarian Pizza":
        ["Pizza sauce",
            "Cheese",
            "Mushrooms",
            "Onions",
            "Olives",
            "Capsicum"]
}


def menu():
    """Get what action the user wants to do.

    This function gets the user to input a number
    with a corrolating action and sends this to a
    function that handles this information. It
    validates input by sending it to a function
    in the input validation module.
    """
    # Checks length of order and displays relevent menu.
    if len(order) == 0:
        menu_choice = inputvalidation.pos_int(
            "1. - Add meal to order\n"
            "2. - Exit\n",
            "Please enter a valid choice (1 or 2)")
        os.system("clear")
        # Calls function that takes the users choice and peforms it.
        evaluate_input(menu_choice, 1)
    elif len(order) >= 1:
        menu_choice = inputvalidation.pos_int(
            "1. - Add meal to order\n"
            "2. - Remove item from order\n"
            "3. - Print order\n"
            "4. - Confirm order\n"
            "5. - Cancel order\n"
            "6. - Exit\n",
            "Please enter a valid choice 1, 2, 3, 4, 5, or 6)")
        os.system("clear")
        evaluate_input(menu_choice, 2)


def cancel_order():
    """Cancel customer order.

    This function cancels a customers
    order by clearing the list saving
    the order information.
    """
    # Clears the list order (customers order).
    order.clear()
    print("Order cancelled")
    time.sleep(1)
    os.system("clear")
    menu()


def print_meals():
    """Format each meal from order.

    This function saves each of the meals the customer has
    ordered and gives each one a number from 1 upwards. This is
    done with a loop and a counter that starts at 1.
    """
    order_items = ""
    # Sets a variable to 1 so it can give options to the user from 1 upwards.
    item_counter = 1
    # Loops for as many meals in order.
    for item in order:
        # Saves a corrosponding number to an item from the list.
        order_items += (f"{item_counter}. - {item[0]}\n")
        item_counter += 1
    order_items += "0. - Exit to menu\n"
    return order_items


def return_to_menu(input_):
    """Check if the program should return to menu.

    This function takes input_ as input and checks
    whether or not the program should return
    back to the menu.

    Parameters:
        input_ (int): Action selected by user.
    """
    # Checks if input passed into function is 0 and acts accordingly.
    if input_ == 0:
        menu()
    else:
        return


def edit_order():
    """Remove item from order.

    This function lets the user remove a meal
    they have added to order. It gets what item
    should be targeted and then loops around
    as many times as there are items in the
    order, unless the targeted item is found
    before that. If this does not occur it
    tries to get the wanted item again.
    """
    print_order(None)
    while True:
        # Displays meals and then asks the
        # operator which one to remove from order.
        targeted_item = inputvalidation.pos_int(
            print_meals() + "\nPlease enter the meal you want to remove: ",
            "You attempted to remove a meal that does not exist, "
            "please try again")
        os.system("clear")
        return_to_menu(targeted_item)
        # Sets a counter to 1 that is used to check what item is targeted.
        option_counter = 1
        # Loops for every item in the customers order.
        for item in order:
            # Checks if targeted item (an integer the user has entered)
            # is the same as option counter.
            if option_counter == targeted_item:
                # Sets targeted item to the item that is causing
                # this iteration of the loop (the item the user wants).
                targeted_item = item
                order.remove(item)
                print("Meal removed")
                option_counter = 0
                break
            option_counter += 1
            # Checks if option counter is greater than the length of the order.
            if option_counter > len(order):
                print("You attempted to remove a meal that does not exist,"
                      " please try again")
        # Checks if option counter has been set to zero,
        # if this has it means that an item
        # has succesfully been removed from the order.
        if option_counter == 0:
            break
    time.sleep(1)
    os.system("clear")
    menu()


def print_menu():
    """Return the menu (restaurant).

    This function gets and saves the menu
    to a variable. In this there is each
    meal with a corrosponding number and
    price.

    Returns:
        printable_menu (str): Restaurant menu formatted.
    """
    printable_menu = ""
    meal_counter = 1
    # For each list in restaurant menu it loops.
    for item in RESTAURANT_MENU:
        # Saves a number that represents a meal
        # then saves the according meal and price from restaurant menu.
        printable_menu += (f"{meal_counter}. - ${item[1]} {item[0]}\n")
        meal_counter += 1
    printable_menu += "0. - Exit to menu\n"
    return printable_menu


def add_meal():
    """Add meal to order.

    This function gets what meal the user wants
    and adds it to the customers order. It does
    this by getting the user to enter a number
    corrosponding to a meal, and then finding
    it through the use of a counter. This is
    later added to order.
    """
    while True:
        # Displays meals and then asks the
        # operator which one the customer wants.
        wanted_meal = inputvalidation.pos_int(
            "Select a meal\n" + print_menu(),
            "Please enter a valid meal option")
        os.system("clear")
        return_to_menu(wanted_meal)
        menu_counter = 1
        # For each item in the restaurants menu this loops.
        for item in RESTAURANT_MENU:
            # Checks if wanted meal (an integer the user has entered)
            # is the same as menu counter.
            if menu_counter == wanted_meal:
                # Sets wanted meal to the item that is causing
                # this iteration of the loop (the item the user wants).
                wanted_meal = item
                # Sets wanted meal to what
                # is returned from the edit meal function.
                wanted_meal = edit_meal(wanted_meal[0], wanted_meal[1])
                order.append(wanted_meal)
                menu_counter = 0
                break
            menu_counter += 1
            # Checks if menu counter is greater than
            # the length of the restaurants menu.
            if menu_counter > len(RESTAURANT_MENU):
                print("You selected a meal that does not exist, "
                      "please try again")
        # Checks if menu counter has been set to zero,
        # if this has it means that an item has
        # succesfully been removed from the order.
        if menu_counter == 0:
            break
    print("Meal added")
    time.sleep(1)
    os.system("clear")
    menu()


def print_ingredients(ingredients):
    """Return a meals ingredients.

    This function saves each ingredient
    specified with a selected meal to a
    variable. It assigns a number to each
    ingredient.

    Parameters:
        ingredients (list): The ingredients of a meal.

    Returns:
        printable_ingredients (str): The formatted ingredients of a meal.
    """
    ingredient_tally = 1
    printable_ingredients = ""
    # Loops for each ingredient in meal ingredients.
    for ingredient in ingredients:
        # Saves ingredient counter and
        # the ingredient that corrosponds to the number.
        printable_ingredients += (f"{ingredient_tally}. - {ingredient}\n")
        ingredient_tally += 1
    return printable_ingredients


def edit_meal(meal, price):
    """Remove an ingredient.

    This function lets the user remove one
    ingredient from an already selected meal. It
    takes meal and price as input, and possibly returns
    an edited meal (or not) and the same price. It gets
    the meals ingredients and which one wants to be removed
    as a number. It then checks each ingredient to find the
    target by looping around and checking if a counter is the
    same as the inputted number for each ingredient in the
    meal.

    Parameters:
        meal (str): Selected meal.
        price (float): Selected meals price:

    Returns:
        meal (str): Selected meal.
        price (float): Selected meals price.
    """
    while True:
        # Asks the operator if they would like to
        # edit the meal they are adding to the customers order.
        ask_operator = inputvalidation.pos_int(
            "Would you like to edit the meal?\n"
            "1. - Yes\n"
            "2. - No\n"
            "0. - Exit to menu\n",
            "You entered an invalid option, please try again")
        os.system("clear")
        return_to_menu(ask_operator)
        if ask_operator == 1:
            # Gets the ingredients from the dictionary and
            # makes a copy of them so they can be edited locally.
            meal_ingredients = MEAL_CONTENTS.get(meal).copy()
            # Asks the user what ingredient they want removed
            # from the meal that is being added to the customers order.
            while True:
                selected_ingredient = inputvalidation.pos_int(
                    print_ingredients(meal_ingredients) +
                    "\nSelect which ingredient you want removed: ",
                    "Please enter a valid ingredient")
                os.system("clear")
                ingredient_counter = 1
                # Loops for each ingredient in the meals ingredients.
                for ingredient in meal_ingredients:
                    # Checks if ingredient counter
                    # (the number corrosponding with an ingredient),
                    # is equal to the users input (selected ingredient).
                    if ingredient_counter == selected_ingredient:
                        meal_ingredients.remove(ingredient)
                        print(f"{ingredient} removed")
                        # Adds what ingredient is being removed
                        # to the meal being added.
                        meal += (f" - no {ingredient} ")
                        return meal, price
                    ingredient_counter += 1
                    # Checks if ingredient counter is bigger
                    # than meal ingredients
                    # (the amount of ingredients in the meal).
                    if ingredient_counter > len(meal_ingredients):
                        print("You attempted to remove an ingredient "
                              "that does not exist, please try again")
        elif ask_operator == 2:
            return meal, price
        else:
            print("You entered an invalid option, please try again")


def get_price():
    """Calculate order price.

    This function gets how much the
    customers order is going to cost.
    It gets the price of each meal
    in order and adds them together,
    later returning this value.

    Returns:
        total_price (float): The cost of the order.
    """
    # Sets price to $0.
    total_price = 0.00
    # Loops for every item (meal, price) in order.
    for item in order:
        # Adds the price from each meal into the total price.
        total_price += item[1]
    return total_price


def print_order(type_):
    """Print the customers order.

    This function prints the customers
    order, this including the total price,
    the price of each singular meal, and
    the ordered amount of each meal.

    Parameters:
        type_ (boolean): Eat-in or takeaway.
    """
    # Gets the total cost and sets it to a variable.
    total_cost = get_price()
    # Checks the variable passed into the function and acts accordingly.
    if type_ is True:
        service_charge = total_cost * SERVICE_CHARGE_PERC
        table_number = random.randint(1, 20)
        total_cost += service_charge
    elif type_ is False:
        customer_name = inputvalidation.check_input(
            "Customer name: ", str, "Please enter a valid name")
        os.system("clear")
    order.sort()
    # Makes and saves a copy of the users order in
    # order to be able to edit it without changing their order.
    printable_order = order.copy()
    print("Oakwood Kitchen\n")
    # Checks the variable passed into the function and acts accordingly.
    if type_ is True:
        print(f"Table: {table_number}")
    elif type_ is False:
        print(f"Name: {customer_name}")
    # For each list in the copy of the users order it loops.
    for item in printable_order:
        # Gets the amount of times a meal appears
        # in the order.
        meal_quantity = printable_order.count(item)
        if meal_quantity != 1:
            # Loops for one less time than the amount of the
            # same meal that is in the copy of the customers order.
            for i in range(meal_quantity - 1):
                printable_order.remove(item)
                i += 1
        # Prints a number for the quantity and then prints out
        # the according meal and price from the customers order.
        print(f"X{str(meal_quantity):3}{item[0]:42}{f"${item[1]}":10}")
    # Checks the variable passed into the function and acts accordingly.
    if type_ is True:
        print(f"{"Eat-in service charge":46}{f"${service_charge:.2f}":10}")
    # Prints out formatting then the total cost of the order.
    print("-" * 56)
    print(f"{"Total:":46}{f"${total_cost:.2f}":10}\n")


def meal_type():
    """Get where the meal is eaten.

    This function gets where the meal
    is going to be eaten from the user.
    From there a variable is assigned as
    true (eat-in) or false (takeaway), and
    returned.

    Returns:
        order_type (boolean): Eat-in or takeaway
    """
    while True:
        order_type = inputvalidation.pos_int(
            "1. - Eat-in\n"
            "2. - Takeaway\n",
            "Please enter a valid option")
        os.system("clear")
        # Checks user input and then sets order type to
        # either true or false.
        if order_type == 1:
            order_type = True
            break
        elif order_type == 2:
            order_type = False
            break
        else:
            print("You entered an invalid option, please try again")
    return order_type


def confirm_order():
    """Confirm customer order.

    This function gets if the user wants
    to confirm their customers order and
    acts accordingly.
    """
    while True:
        # Asks operator if they want to confirm order, saves this to variable.
        check_confirmation = inputvalidation.pos_int(
            "Are you sure you want to confirm the order?\n"
            "1. - Yes\n"
            "2. - No\n",
            "Please enter a valid option (1 or 2)")
        os.system("clear")
        # Checks if the operator wants to confirm order or not.
        if check_confirmation == 1:
            print("Order confirmed")
            os.system("clear")
            # Prints customer order after asking if it is eat-in or takeaway.
            print_order(meal_type())
            input("Hit return or enter to continue")
            os.system("clear")
            # Clears the list containing the customers order.
            order.clear()
            menu()
            break
        elif check_confirmation == 2:
            menu()
            break
        else:
            print("You entered an invalid option, please try again")


def evaluate_input(choice, menu_type):
    """Do action from input.

    This function takes choice and iteration as input and
    takes an action based on the input.

    Parameters:
        choice (int): The users choice from the menu.
        iteration (int): Menu 1 or menu 2
    """
    # Checks what iteration/situation needs to be evaluated.
    if menu_type == 1:
        while True:
            # Checks operator input and acts accordingly.
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                sys.exit("The program has ended")
            else:
                print("You entered a choice that does not exist,"
                      " please try again")
                menu()
                break
    elif menu_type == 2:
        while True:
            # Checks operator input and acts accordingly.
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                edit_order()
                break
            elif choice == 3:
                print_order(None)
                input("Hit return or enter to continue")
                os.system("clear")
                menu()
                break
            elif choice == 4:
                confirm_order()
                break
            elif choice == 5:
                cancel_order()
                break
            elif choice == 6:
                sys.exit("The program has ended")
            else:
                print("You entered a choice that does not exist,"
                      " please try again")
                menu()
                break


os.system("clear")
menu()
