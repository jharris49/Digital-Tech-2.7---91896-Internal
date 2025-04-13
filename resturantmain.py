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

def menu(iteration):
    """
    """
    if iteration == 1:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Exit\n", "Please enter a valid choice (1, 2, or 3)")
        evaluate_input(menu_choice, 1)
    elif iteration == 2:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Edit order\n3. - Print order\n4. - Confirm order\n5. - Exit\n", "Please enter a valid choice (1, 2, 3, 4, or 5)")
        evaluate_input(menu_choice, 2)
    
def edit_order():
    print("Edit order")

def add_meal():
    """
    """
    os.system("clear")
    print_menu()
    wanted_meal = inputvalidation.pos_int("", "Please entere a valid meal option")
    while True:
        if wanted_meal == 1:
            selected_meal = restaurant_menu[0]
            order.append(selected_meal)
            print(order)
            break
        elif wanted_meal == 2:
            selected_meal = restaurant_menu[1]
            order.append(selected_meal)
            print(order)
            break
        elif wanted_meal == 3:
            selected_meal = restaurant_menu[2]
            order.append(selected_meal)
            print(order)
            break
        else:
            print("You selected a meal that does not exist, please try again")
            add_meal()
            break
    print("Meal added")
    time.sleep(1)
    os.system("clear")
    menu(2)
    

def edit_meal():
    print("Edit Meal")

def get_price():
    print("Get price")

def print_menu():
    """
    """
    meal_counter = 1
    for item in restaurant_menu:
        print(f"{meal_counter}. - ${item[1]} {item[0]}")
        meal_counter += 1

def print_order():
    print("Print order")

def confirm_order():
    print("Confirm order")

def evaluate_input(choice, iteration):
    """
    """
    if iteration == 1:
        while True:
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                sys.exit("The program has ended")
            else:
                print("You entered a choice that does not exist, please try again")
                menu(1)
    elif iteration == 2:
        while True:
            if choice == 1:
                add_meal()
                break
            elif choice == 2:
                edit_order()
                break
            elif choice == 3:
                print_order()
                break
            elif choice == 4:
                confirm_order()
                break
            elif choice == 5:
                sys.exit("The program has ended")
            else:
                os.system("clear")
                print("You entered a choice that does not exist, please try again")
                menu(2)


menu(1)

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
