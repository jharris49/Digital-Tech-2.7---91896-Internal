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

def menu(iteration):
    """
    """
#checks what menu is applicable for the operators situation and acts accordingly
    if iteration == 1:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Exit\n", "Please enter a valid choice (1 or 2)")
        #calls function that acts accordingly to what the operator asks for
        evaluate_input(menu_choice, 1)
    elif iteration == 2:
        menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Edit order\n3. - Print order\n4. - Confirm order\n5. - Exit\n", "Please enter a valid choice (1, 2, 3, 4, or 5)")
        evaluate_input(menu_choice, 2)
    
def edit_order():
    print("Edit order")


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
    #creates a variable that saves what meal the operator wants 
    wanted_meal = inputvalidation.pos_int(print_menu(), "Please enter a valid meal option")
    while True:
        #checks what meal the operator has selected and acts accordingly
        if wanted_meal == 1:
            #saves the chosen meal from restaurant menu to a variable 
            selected_meal = restaurant_menu[0]
            #adds this meal to the customers order
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
    total_price = 0.00
    for item in order:
        total_price += item[1]   
    total_price = round(total_price, 2)
    return total_price


def print_order():
    """
    """
    os.system("clear")
    order.sort()
    total_cost = get_price()
    print("Restaurant Name")
    print("Order:") 
#for each list in restaurant menu it loops
    for item in order:
        meal_quantity = order.count(item)
        if meal_quantity != 1:
            for i in range(meal_quantity - 1):
                order.remove(item)
                i += 1
        #prints a number that represents then prints out the according meal and price from user order
        print(f"X{str(meal_quantity):2s}{item[0]:10s}${item[1]}")
    print("-----------------")
    print(f"{"Total:":13}${total_cost}\n")


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
            continue_on = input("Hit return to continue")
            order.clear()
            os.system("clear")
            menu(1)
            break
        elif check_confirmation == 2:
            os.system("clear")
            menu(2)
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
                menu(1)
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
                break

os.system("clear")
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
