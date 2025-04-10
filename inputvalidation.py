import time

def check_input(message, variety, error_message):
    while True:
        try:
            user_choice = variety(input(message))
            return user_choice
        except:
            print(error_message)

def pos_int(message, error_message):
    while True:
        try:
            user_choice = int(input(message))
            if user_choice < 0:
                print(error_message)
                time.sleep(1)
                continue
            else:   
                return user_choice
        except:
            print(error_message)