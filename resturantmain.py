#imports modules including my own input validation one that checks if user input
import inputvalidation, time, os, sys

restaurant_menu = [
    ("item 1", 9.99), 
    ("item 2", 8.99), 
    ("item 3", 15.99)]

order = [

]

meal_contents = {
    "item 1": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 2": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 3": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 4": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 5": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 6": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 7": ["ingredient 1", "ingredient 2", "ingredient 3"],
    "item 8": ["ingredient 1", "ingredient 2", "ingredient 3"],
}

def menu():
    """
    """
    print("At menu")
#checks what menu is applicable for the operators situation and acts accordingly
    if len(order) == 0:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Exit\n", "Please enter a valid choice (1 or 2)")
        os.system("clear")
        #calls function that acts accordingly to what the operator asks for
        evaluate_input(menu_choice, 1)
    elif len(order) >= 1:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Remove item from order\n3. - Print order\n4. - Confirm order\n5. - Exit\n", "Please enter a valid choice (1, 2, 3, 4, or 5)")
        os.system("clear")
        evaluate_input(menu_choice, 2)


def print_meals():
    """
    This function prints each meal that is in the customers order and assigns a number to it
    """
    #sets a variable to one so it can give options to the user from 1 upwards
    item_counter = 1
#for each item in the customers order this loops
    for item in order:
        #prints out a number and an item from the list that now corrso=ponds to that number
        print(f"{item_counter}. - {item[0]}")
        item_counter += 1


def edit_order():
    print_order()
    while True:
        print_meals()
        #asks the operator what item they want to be removed from the order
        targeted_item = inputvalidation.pos_int("Please enter the meal you want to remove: ", "You attempted to remove a meal that does not exist, please try again")
        #sets a counter to 1 that is used to check what item is targeted
        option_counter = 1
        for item in order:
        #checks if targeted item (an integer the user has entered) is the same as option counter and then acts accordingly
            if option_counter == targeted_item:
                #sets targeted item to the item that is causing this iteration of the loop (the item the user wants) 
                targeted_item = item
                order.remove(item)
                print("Meal removed")
                option_counter = 0
                break
        #checks if option counter is greater than the length of the order. If it is, it means that the option the user has entered does not exist.
            option_counter += 1   
            if option_counter > len(order):
                os.system("clear")
                print("You attempted to remove a meal that does not exist, please try again")   
    #checks if option counter has been set to zero, if this has it means that an item has succesfully been removed from the order
        if option_counter == 0:
            break
    os.system("clear")
    menu()


def print_menu():
    """
    """
    printable_menu = ""
    meal_counter = 1
#for each list in restaurant menu it loops
    for item in restaurant_menu:
        #saves a number that represents a meal then saves the according meal and price from restaurant menu
        printable_menu += (f"{meal_counter}. - ${item[1]} {item[0]}\n")
        meal_counter += 1
    return printable_menu


def add_meal():
    """
    """
    print("Adding meal")
    #creates a variable that saves what meal the operator wants 
    while True:
        #asks the operator what item the customer wants
        wanted_meal = inputvalidation.pos_int(print_menu(), "Please enter a valid meal option")
        os.system("clear")
        menu_counter = 1
     #for each item in the restaurants menu this loops
        for item in restaurant_menu:
        #checks if wanted meal (an integer the user has entered) is the same as menu counter and then acts accordingly
            if menu_counter == wanted_meal:
                #sets wanted meal to the item that is causing this iteration of the loop (the item the user wants) 
                wanted_meal = item
                wanted_meal = edit_meal(wanted_meal[0], wanted_meal[1])
                order.append(wanted_meal)
                menu_counter = 0
                break
        #checks if menu counter is greater than the length of the restaurants menu. If it is, it means that the meal the user has entered does not exist.
            menu_counter += 1  
            if menu_counter > len(restaurant_menu):
                os.system("clear")
                print("You selected a meal that does not exist, please try again")   
    #checks if option counter has been set to zero, if this has it means that an item has succesfully been removed from the order 
        if menu_counter == 0:
            break
    print("Meal added")
    time.sleep(1)
    os.system("clear")
    menu()
    

def edit_meal(meal, price):
    """
    """
    while True:
        print(meal)
        #asks the operator if they would like to edit the meal they are adding to the customers order
        ask_operator = inputvalidation.pos_int("Would you like to edit the meal?\n1. - Yes\n2. - No\n", "You entered an invalid option, please try again")
        os.system("clear")
    #checks if the operator wants to edit the meal they are adding
        if ask_operator == 1:
            #gets the ingredients from the dictionary and makes a copy of them
            meal_ingredients = meal_contents.get(meal).copy()
            print(meal_ingredients)
            ingredient_counter = 1
        #loops for each ingredient in meal ingredients
            for ingredient in meal_ingredients:
                #prints ingredient counter and the ingredient that corrosponds to the number
                print(f"{ingredient_counter}. - {ingredient}")
                ingredient_counter += 1
            #asks the user what ingredient they want removed from the meal that is being added to the customers order
            selected_ingredient = inputvalidation.pos_int("Select which ingredient you want removed: ", "Please enter a valid ingredient")
            ingredient_counter = 1
        #loops for each ingredient in ingredient
            for ingredient in meal_ingredients:
            #checks if ingredient counter (the number corrosponding with an ingredient), is equal to the users input (selected ingredient) and acts accordingly
                if ingredient_counter == selected_ingredient:
                    #removes the ingredient from the meals ingredients
                    meal_ingredients.remove(ingredient)
                    print(f"{ingredient} removed")
                    #adds what ingredient is being removed to the meal being added
                    meal += (f" - no {ingredient} ")
                    print(meal)
                    #returns the new information regarding the meal 
                    os.system("clear")
                    return meal, price
                ingredient_counter += 1
            #checks if ingredient counter is bigger than meal ingredients (the amount of ingredients in the meal)
                if ingredient_counter > len(meal_ingredients):
                    os.system("clear")
                    print("You attempted to remove an ingredient that does not exist, please try again")  
        elif ask_operator == 2:
            os.system("clear")
            return meal, price
        else:
            os.system("clear")
            print("You entered an invalid option, please try again")  


def get_price():
    """
    """
    #sets price to $0
    total_price = 0.00
#loops for every item (meal, price) in order
    for item in order:
        #adds the price from each meal into the total price
        total_price += item[1]   
    #rounds price to 2 decimal points as it is a monetary amount and to prevent floating point errors
    total_price = round(total_price, 2)
    return total_price


def print_order():
    """
    """
    print("Printing order")
    os.system("clear")
    order.sort()
    #makes and saves a copy of the users order in order to be able to edit it without changing their order
    printable_order = order.copy()
    print(printable_order)
    #gets the total cost and sets it to a variable
    total_cost = get_price()
    print("Restaurant Name")
    print("Order:") 
#for each list in the copy of the users order it loops
    for item in printable_order:
        #gets the amount of times a meal appears in the order and saves it to a variable
        meal_quantity = printable_order.count(item)
        if meal_quantity != 1:
        #loops for one less time than the amount of the same meal that is in the copy of the customers order
            for i in range(meal_quantity - 1):
                #removes the item from the copy of the customers order
                printable_order.remove(item)
                i += 1
        #prints a number that represents then prints out the according meal and price from user order
        print(f"X{str(meal_quantity):3s}{item[0]:10s}${item[1]}")
    print("-----------------")
    print(f"{"Total:":13}${total_cost}\n")
    print(order)
    print(printable_order)


def confirm_order():
    """
    """
    os.system("clear")
    while True:
        #asks operator if they want to confirm order, saves this to variable
        check_confirmation= inputvalidation.pos_int("Are you sure you want to confirm the order?\n1. - Yes\n2. - No\n", "Please enter a valid option (1 or 2)")
#checks if the operator wants to confirm order or not
        if check_confirmation == 1:
            print("Order confirmed")
            #prints customer order
            print_order()
            continue_on = input("Hit return or enter to continue")
            #clears the list containing the customers order
            order.clear()
            os.system("clear")
            menu()
            break
        elif check_confirmation == 2:
            os.system("clear")
            menu()
            break
        else:
            print("You entered an invalid option, please try again")
            time.sleep(2)


def evaluate_input(choice, iteration):
    """
    """
#checks what iteration/situation needs to be evaluated
    if iteration == 1:
        while True:
        #checks if operator input and acts accordingly
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                sys.exit("The program has ended")
            else:
                print("You entered a choice that does not exist, please try again")
                #returns to main menu
                menu()
                break
    elif iteration == 2:
        while True:
         #checks if operator input and acts accordingly
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                edit_order()
                break
            elif choice == 3:
                print_order()
                continue_on = input("Hit return or enter to continue")
                os.system("clear")
                menu()
                break
            elif choice == 4:
                confirm_order()
                break
            elif choice == 5:
                sys.exit("The program has ended")
            else:
                os.system("clear")
                print("You entered a choice that does not exist, please try again")
                menu()
                break

os.system("clear")
menu()

"""
Print menu. Let operator select what they want to do: 
add desert, add starter, add main, exit program, cancel order (when applicable), confirm order (when applicable)
check if input is valid then evaluate operator input  
act on opertor input
return to menu

functions:
    add meal - desert, main, starter, etc:
        print out all of the meal options and ask the operator to what meal they want to add to the order
        check if input is valid then evaluate operator input 
        ask operator if they want to edit meal and what they want to edit
        check if input is valid then evaluate operator input 
        act on operator input
        add chosen meal to order
        return to menu
    
    edit meal
        print out ingredients avaliable to be added along with the option to remove something and the option to exit this page
        check if input is valid then evaluate operator input 
        add selected items (if applicable) or ask the operator what they want removed from the meal
        check if input is valid then evaluate operator input 
        act on operator input
    
    print order
        loop through each value in list order and print it
        calculate total and print it at bottom
        format this like a receipt
        
    get price
        loop through each value in list order and get the price of each item from it
        add these togethor and save to variable total cost
        return this value
    
    evaluate input
        check user choices in if statement
        undergo action from this choice

lists:
    menu = (meal 1, price), (meal 2, price), (meal 3, price), (meal 4, price) etc
    order = (ordered meal 1, price), (ordered meal 2, price) etc

dictionarys:
    meal contents = {
        meal 1: [ingredient 1, ingredient 2, ingredient 3, etc]
        meal 2: [ingredient 1, ingredient 2, ingredient 3, etc]
        meal 3: [ingredient 1, ingredient 2, ingredient 3, etc]
        etc
    }
"""
