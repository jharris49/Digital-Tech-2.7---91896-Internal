import inputvalidation, time, os

restaurant_menu = [
    ("item 1", "price (is a float)"), 
    ("item 2", "price is a float)"), 
    ("item 3", "price (is a float)")]

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
    menu_choice = inputvalidation.pos_int("1. - Add meal to order\n2. - Edit order\n3. - Print order\n4. - Confirm order\n5. - Exit", "Please enter a valid choice (1, 2, 3, 4, or 5)")
    evaluate_input(menu_choice, 1)

def add_meal():
    print("Placeholder")

def edit_meal():
    print("Placeholder")

def get_price():
    print("Placeholder")

def print_order():
    print("Placeholder")

def evaluate_input(choice, iteration):
    print("Placeholder")



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
