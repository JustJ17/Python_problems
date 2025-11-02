import csv
import os

def temp_menu():
    print("""
        ==============================
        Temperature convertor
            1. Celsius to Fahrenheit
            2. Fahrenheit to Celsius
            3. Celsius to Kelvin
            4. Kelvin to Celsius
            0. Exit
        ===============================
""")
    
def selection_handler():
    while True:
        temp_menu()
        selection = input("Choose conversion (1-4) or choose (0) to exit: ")
        if selection == "1":
            Cel_to_Fhr()
        elif selection == "2":
            Fhr_to_Cel()
        elif selection == "3":
            Cel_to_kel()
        elif selection == "4":
            Kel_to_Cel()
        elif selection == "0":
            return
        else:
            print("Invalid Input!")

def Cel_to_Fhr():
    temp = take_temp("C")
    nTemp = (temp * (9/5)) + 32
    print(f"{temp:.1f}°C = {nTemp:.1f}°F")

def Fhr_to_Cel():
    temp = take_temp("F")
    nTemp = (temp -32) * (5/9)
    print(f"{temp:.1f}°F = {nTemp:.1f}°C")

def Cel_to_kel():
    temp = take_temp("C")
    nTemp = temp +273.15
    print(f"{temp:.1f}°C = {nTemp:.1f} K")

def Kel_to_Cel():
    temp = take_temp("K")
    nTemp = temp -273.15
    print(f"{temp:.1f}K = {nTemp:.1f}°C")

def take_temp(temp_type):
    while True:
        Temp = input("Enter Temperature: ")
        try:
            Temp = int(Temp)
        except ValueError:
            print("Temp must be a number!")
        if temp_type == "K":
            if Temp < 0:
                print("Temperature in Kelvin must be above 0!")
            else:
                return Temp
        elif temp_type == "C":
            if Temp < -273:
                print("Temperature in Celsius must be above -273!")
            else:
                return Temp
        elif temp_type == "F":
            if Temp < -460:
                print("Temperature in Fahrenheit must be above -460!")
            else:
                return Temp

def arthimatic_operations():
    nums = input("Enter numbers separated by spaces: ").strip()
    nums = nums.split()
    nums_int = [int(x) for x in nums]
    nums_no_dups = set(nums_int)
    print(f"sum: {sum(nums_int)}")
    print(f"Average: {sum(nums_int)/len(nums_int):.2f}")
    print(f"Max: {max(nums_int)}   Min: {min(nums_int)}")
    print(f"No duplicates: {nums_no_dups}")
    print(f"Sorted: {sorted(nums_int)}")
    print(f"Even: {[x for x in nums_int if x%2==0]}")
    print(f"Odd: {[x for x in nums_int if x%2!=0]}")

def string_operations():
    user_str = input("Enter Text:")
    print(f"Total characters (with spaces): {len(user_str)}")
    print(f"Total characters (without spaces) : {len(user_str.replace(' ', ''))} ")
    print(f"Words Count: {len(user_str.strip().split(' '))}")
    str_list = list(user_str.replace(' ', '').lower())
    str_dict = {}
    for c in str_list:
        if c in str_dict:
            str_dict[c] += 1
        else:
            str_dict[c] = 1
    maxAppearances = max(str_dict.values())
    print(f"character frequency: {str_dict}")
    freq = list()
    for c in str_dict:
        if str_dict[c] == maxAppearances:
            freq.append(c) 
            
    print(f"Most common character/s: {freq} (Appeared {maxAppearances} times)") 
    reverse_str = user_str.strip()[::-1]
    if(reverse_str == user_str.strip()):
        print("Is palindrome: Yes")
    else:
        print("Is palindrome: No")
    print(f"Reversed string: {reverse_str}")

def guessing_game():
    import random

    attempts_left = 7
    print("Welcome to Number Guessing Game!")
    while True:
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {attempts_left} attempts.")
        attempts_used = 0
        guessed_number = round((random.random()*100))
        while True:
            attempts_used += 1
            print(f"Attempt {attempts_used} - Your Guess: ", end="")
            try:
                guess = int(input())
            except ValueError:
                print("You can only enter a number!")
            if guess > 100 or guess < 0:
                print("You must guess a number between 0 and 100!")
            
            if (guess == guessed_number):
                print(f"Congratulations! You guessed it in {attempts_used} attempts!")
                break
            elif (guess < guessed_number and attempts_used < attempts_left):
                print("Too low! Try Again")
            elif (guess > guessed_number and attempts_used < attempts_left):
                print("Too High!, Try Again")
            elif (attempts_used >= attempts_left):
                print(f"Game Over! The number was {guess}")
                break
        while True:    
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "y":
                break
            elif play_again.lower() == "n":
                return
            else:
                print("Invlaid Input!")

def shopping_menu():
        print("""
                ==============================
                Shopping Cart
                    1. Add items 
                    2. Remove items
                    3. Update quantity
                    4. View cart
                    5. Checkout
                    0. Exit
                ===============================
            """, end="")

def add_items(cart):
    i_name = input("Insert the Item name: ")
    while True:
        i_price = input("Insert the Item price: ")
        try:
            i_price = int(i_price)
        except ValueError:
            print("The Price field can only accept numbers!")
            continue
        if i_price < 0:
            print("The item price must be a positive number!")
        else:
            break
    while True:
        i_quantity = input("Insert the Item Quantity: ")
        try:
            i_quantity = int(i_quantity)
            break
        except ValueError:
            print("The Quantity field can only accept numbers!")
        if i_quantity < 1:
            print("The item price must be larger than 0!")
    if i_name not in cart:
        cart[i_name] = {"price" : i_price, "quantity" : i_quantity }
        print(f"Your Item {i_name} was added!")
        return cart
    else:
        while True:
            choice = input(f"You already have an Item with the same name! would you like to replace the existing item? (y/n) : ")
            if choice.lower() == "y":
                cart[i_name]["quantity"] = i_quantity
                cart[i_name]["price"] = i_price
                print("Your Item was updated!")
                return cart
            elif choice.lower() == "n":
                print("Aborting...")
                return cart
            else:
                print("Invalid choice")

def remove_item(cart):
    keys = cart.keys()
    print("Select which Item would you like to remove")
    keys_list = list()
    for i,key in enumerate(keys):
        print(f"{i+1}.{key}")
        keys_list.append(key)
    while True:
        selection = input("your choice: ")
        try:
            selection = int(selection)
            if keys_list[selection-1]:
                print(f"The item named {keys_list[selection-1]} have been removed!")
                del cart[keys_list[selection-1]]
                return cart
            else:
                print("Choice out of range")
        except ValueError: 
            print("invalid Input!")

def update_quantity(cart):
    keys = cart.keys()
    print("Select which Item would you like to update: ")
    keys_list = list()
    for i,key in enumerate(keys):
        print(f"{i+1}.{key}")
        keys_list.append(key)
    while True:
        selection = input("your choice: ")
        try:
            selection = int(selection)
            if selection-1 in range(len(keys_list)):
                new_Q = input("Enter the new Quantity Value: ")
                cart[keys_list[selection-1]]["quantity"] = new_Q
                print(f"The item named {keys_list[selection-1]} have been updated!")
                return cart
            else:
                print("Choice out of range")
        except ValueError: 
            print("invalid Input!")

def view_cart(cart):
    print(" -------------------------Cart Summary-------------------------")
    print("       Item      Qty       price     Total")
    for item in cart:
        print(f'{item:>10}{cart[item]["quantity"]:>10}{cart[item]["price"]:>10}{cart[item]["quantity"] * cart[item]["price"]: >10,.2f} $')

def checkout(cart):
    total=0
    for item in cart:
        total += cart[item]["quantity"] * cart[item]["price"]
    print(f"Subtotal = {total}")
    if total > 300:
        discounted_total = total *0.9
        print(f"Total after discount: {discounted_total}")

def shopping_cart():
    my_cart = dict()
    while True:
        shopping_menu()
        selection = input("Choose option (1-5) or choose (0) to exit: ")
        if selection == "1":
            add_items(my_cart)
        elif selection == "2":
            remove_item(my_cart)
        elif selection == "3":
            update_quantity(my_cart)
        elif selection == "4":
            view_cart(my_cart)
        elif selection == "5":
            checkout(my_cart)
        elif selection == "0":
            return
        else:
            print("Invalid Input!")

def conact_book_menu():
        print("""
                ==============================
                    Contact Book manager
                    1. Add conact
                    2. View All Contacts
                    3. Search Contact
                    4. Delete Contact
                    5. Update Contact
                    0. Exit
                ===============================
            """, end="")

def add_contact():
    conatct_name = input("Insert the contact name: ")
    while True:
        contact_phone = input("Insert the conact phone: ")
        try:
            contact_phone = int(contact_phone)
            break
        except ValueError:
            print("The phone field can only accept numbers!")
            continue
    contact_email = input("Insert the contact email: ")
    with open ('contacts.csv', 'a', newline='') as contacts:
        writer = csv.writer(contacts,delimiter="|")
        writer.writerow([conatct_name,contact_phone,contact_email])

def view_contact():
    with open ('contacts.csv', 'r', newline='') as contacts:
        reader = csv.reader(contacts, delimiter='|')
        for row in reader:
            print(row)

def search_contact():
    while True:
        selection = input("Would you like to search by name or phone numer ? (1 for name, 2 for phone number): ")
        if(selection not in ["1","2"]):
            print("Invalid input! Please choose either 1 or 2")
        else:
            selection = int(selection)
        if selection == 1:
            name = input("Please enter the name you are searching for: ")
            break
        if selection == 2:
            while True:
                contact_phone = input("Insert the contact phone you are looking for: ")
                try:
                    int(contact_phone)
                    break
                except ValueError:
                    print("The phone field can only accept numbers!")
                    continue
            break
            
    with open('contacts.csv', 'r', newline='') as contacts:
        reader =csv.reader(contacts, delimiter='|')
        for row in reader:
            if selection == 1:
                if row[selection-1] == name:
                    print(row)
                    return        
            if selection == 2:
                if row[selection-1] == contact_phone:
                    print(row)
                    return
    print("contact not found")
    return
            

    
def contact_book_manager():
    while True:
        path = "contacts.csv"
        if( not os.path.exists(path)):
            fields = ["Name","Phone","Email"]
            with open ('contacts.csv', 'a', newline='') as contacts:
                writer = csv.writer(contacts, delimiter='|')
                writer.writerow(fields) 
        conact_book_menu()
        selection = input("Choose option (1-5) or choose (0) to exit: ")
        if selection == "1":
            add_contact()
        elif selection == "2":
            view_contact()
        elif selection == "3":
            search_contact()
        elif selection == "4":
            view_cart()
        elif selection == "5":
            checkout()
        elif selection == "0":
            return
        else:
            print("Invalid Input!")

# selection_handler()

# arthimatic_operations()

# string_operations()

# guessing_game()

# shopping_cart()

contact_book_manager()
    