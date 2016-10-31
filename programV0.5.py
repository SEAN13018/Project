# Menu V0.5
# 1/11/16
# Sean Nichols

from random import randint
import sqlite3
import string
import itertools
import time

# Why there functions are separated in this program where you order food. 
# There are separate functions for ordering food and drinks as by separating the two, 
# It improves the user's experience where I can easily describe the product to the user by calling the items either "food" or "drinks".
# Also by having 2 separate functions the layout of the code is simpler in comparison to having it in one function. 


# The reset function removes data from the database created by other times the program has been run.
# To avoid interference with the new user's ordering experience.
# (Only the current user's items are present on the database)
def reset():
    with sqlite3.connect("project_Database.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Food SET Quantity = 0")
        cursor.execute("UPDATE Drink SET Quantity = 0")
        cursor.execute("DELETE FROM Other")
        # Resets the data entered by the user.

        
# The lists function creates lists containing data from the database.
# Lists that are made global, so the other functions in the program can access them. 
def lists():
    with sqlite3.connect("project_Database.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT Name_lower FROM Food")
        global itemList
        itemList = list(itertools.chain(*cursor.fetchall()))
        cursor.execute("SELECT Price FROM Food")
        global priceList
        priceList = list(itertools.chain(*cursor.fetchall()))
        cursor.execute("SELECT Name_lower FROM Drink")
        global itemList_2
        itemList_2 = list(itertools.chain(*cursor.fetchall()))
        cursor.execute("SELECT Price FROM Drink")
        global priceList_2
        priceList_2 = list(itertools.chain(*cursor.fetchall()))



# This function asks and remembers what the user would like to do. Then sends them to the setup function.  
def main():
    print("Welcome to Sean's Program: Menu V0.5 \n")
    print("PROMOTION: There is a chance of getting your order for free...")
    print("disclaimer: The promotional chance refers to the current user's randomised order number matching a previously selected 4 digit number created by the programmer \n \n") 
    print("Menu Options: \nFood \nDrinks \nOwn Items")
    question = input("What would you like to order? : \n ")
    question = question.lower()
    if question == "food":
        task = 1
        setup(task);
    elif question == "drinks" or question == "drink":
        task = 2
        setup(task)
    elif question == "own items" or question == "own" or question == "own item": 
        task = 3
        setup(task)
    else:
        print("Please enter a valid option")
        print("Sending you back to the beginning")
        print("__________________________________________")
        main()
        # Sends the user to the setup function



# The setup function utlises the reset and lists functions and sends the user to do what they have inputted in the main function. 
def setup(task):
    reset()
    lists()
    totalPrice = 0
    if task == 1:
        food(totalPrice, task);
    elif task == 2:
        drinks(totalPrice, task);
    elif task == 3:
        misc(totalPrice, task);
     # Sends correct parameters to functions   



# The food function allows the user to order food.
# Food is a separate function because of string formatting that personalises the order for the correct item type. e.g. it prints "The current food items available:"
def food(totalPrice, task):
    global itemList
    global priceList
    question = "y"
    while question == "y" or question == "yes": 
        print("_____________________________________________")  
        print("Total price of your food items ${0}\n".format(totalPrice))
        print("The current food items available: \n")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Food")
            items = cursor.fetchall()
        for row in items:
            print("{0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("Please select one food item at a time.")
        # Prints the items available for ordering
        question_1 = input("What food item would you like? \n ").lower()
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price FROM Food WHERE Name_lower = '{0}'".format(question_1))
            check = cursor.fetchall()
            # Checks if there is an item, that the user has requested, on the database
            if len(check) == 0:
                question = "y"
                print("This is not a valid input")
            else:
                question = "q"
        while question == "q":
            print("\nPlease enter a value between 1 & 15")
            question_2 = input("How many {0} do you want? \n ".format(question_1))
            if question_2.isdigit():
                question_2 = int(question_2)
            # Quantity must be between 1 and 15
                if 1 <= question_2 <= 15:
                    with sqlite3.connect("project_Database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("SELECT Quantity FROM Food WHERE Name_lower = '{0}'".format(question_1))
                        quantity = list(itertools.chain(*cursor.fetchall()))
                        quantity = question_2 + quantity[0]
                        cursor.execute("UPDATE Food SET Quantity = {0} WHERE Name_lower = '{1}'".format(quantity, question_1))
                        # The quantity has been updated on the database file
                        
                        identifier = itemList.index(question_1)
                        total = quantity * priceList[identifier]
                        totalPrice = totalPrice + total 
                        print("\nCurrent order total = ${0}".format(totalPrice))
                        question = "x"

    while question == "x":
        # Make it so it returns them back to the while when entering the wrong thing.
        question = input("Do you want to order more food? yes / no: ")
        question = question.lower()            # Ignored the no after the second item is entered - FIXED
        if question == "y" or question == "yes":
            question = "z"
            food(totalPrice, task)
        elif question == "n" or question == "no":
            question = "z"
            print("_____________________________________________")
            end(totalPrice, task)
            # It sends them to the final (end) function
        else:
            # Enters second item, then chooses no - deletes item from list? - FIXED (removed list causing problem)
            # If the user does not want to continue entering items - FIXED  (removed list with problem)               
            print("Please choose a valid option...  y/n ")
            question = "x"



# The drinks function allows the user to order drinks. 
# There are separate functions for ordering food and drinks as by separating the two, 
# It improves the user's experience where I can easily describe the product to the user by calling the items either "food" or "drinks".
# Also by having 2 separate functions the layout of the code is simpler in comparison to having it in one function. 
def drinks(totalPrice, task):
    # Input not registering 14/09/16 - Working
    global itemList_2
    global priceList_2
    question = "y"
    while question == "y" or question == "yes": 
        print("_____________________________________________")  
        print("Total price of your drink items ${0}\n".format(totalPrice))
        print("The current drinks available: \n")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Drink")
            items = cursor.fetchall()
        for row in items:
            print("{0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("Please select one drink at a time.")
        # Prints the items available for ordering
        question_1 = input("What drink would you like? \n ").lower()
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price FROM Drink WHERE Name_lower = '{0}'".format(question_1))
            check = cursor.fetchall()
            # Checks if there is an drink, that the user has entered, in the database
            if len(check) == 0:
                question = "y"
                print("This is not a valid input")
            else:
                question = "q"
        while question == "q":
            print("\nPlease enter a value between 1 & 15")
            question_2 = input("How many {0} do you want? \n ".format(question_1))
            if question_2.isdigit():
                question_2 = int(question_2)
            # Quantity must be between 1 and 15
                if 1 <= question_2 <= 15:
                    with sqlite3.connect("project_Database.db") as db:
                        cursor = db.cursor()
                        cursor.execute("SELECT Quantity FROM Drink WHERE Name_lower = '{0}'".format(question_1))
                        quantity = list(itertools.chain(*cursor.fetchall()))
                        quantity = question_2 + quantity[0]
                        cursor.execute("UPDATE Drink SET Quantity = {0} WHERE Name_lower = '{1}'".format(quantity, question_1))
                        # The quantity has been updated on the database file
                        
                        identifier = itemList_2.index(question_1)
                        total = quantity * priceList_2[identifier]
                        totalPrice = totalPrice + total 
                        print("\nCurrent order total = ${0}".format(totalPrice))
                        question = "x"

    while question == "x":
        # Make it so it returns them back to the while when entering the wrong thing.
        question = input("Do you want to order more drinks? yes / no: ")
        question = question.lower()            # Ignored the no after the second item is entered - FIXED
        if question == "y" or question == "yes":
            question = "z"
            food(totalPrice, task)
        elif question == "n" or question == "no":
            question = "z"
            print("_____________________________________________")
            end(totalPrice, task)
            # It sends them to the final (end) function
        else:
            # Enters second item, then chooses no - deletes item from list? - FIXED
            # If the user does not want to continue entering items - FIXED                
            print("Please choose a valid option...  y/n ")
            question = "x"



# The misc function allows the users to create their own items and order them. 
def misc(totalPrice,task):
    print("_____________________________________________")  
    question = "y"
    while question == "yes" or question == "y":
        print("Total price of your items ${0}\n".format(totalPrice))
        print("The current items available: ")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Other")
            items = cursor.fetchall()
        for row in items:
            print("{0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        false = "no"
        while false == "no":
            print("Please enter one item at a time.")
            item = input("What is the name of the new item? \n ").capitalize()
            with sqlite3.connect("project_Database.db") as db:
                cursor = db.cursor()
                cursor.execute("SELECT Name FROM Other WHERE Name = '{0}'".format(item))
                check = cursor.fetchall()
                # Checks if there is an item, that the user has entered, in the database
            if len(check) == 0:
                false = "yes"
            else:
                print("Please do not repeat item names.\n")
        # Check if the same is already in the program If so ask for a new name.
        
        # Makes sure that the price is a float type (a number/decimal)
        while false == "yes":
            price = input("What is the price of the item? Please restrict prices to a maximum of $99.99 \n $")
            try:
                price = float(price)
            except ValueError:
                false = "yes"
            else:
                # The price must be greater than $0 but less than $100
                if 0 < price <= 99.99:
                    false = "no"
        while false == "no":
            quantity = input("How many would you like? \n")
            # The quantity must be an integer that is equal to or greater than 1 or equal to or less than 15
            if quantity.isdigit():
                quantity = int(quantity)
                if 1 <= quantity <= 15:
                    total = quantity * price
                    false = "b"
                else:
                    print("Please enter a quantity between 1 and 15. ")

        new = item, price, quantity
        # Adds the name of the item, it's price, and the quantity onto the database
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO Other(Name, Price, Quantity) VALUES(?,?,?)",new)
        print("{0} {1}(s) has been added for ${2}".format(quantity, item, total))
        totalPrice = totalPrice + total
        question = "confirm"
        while question == "confirm":
            question_1 = input("Would you like to add another item? yes/no \n").lower()
            if question_1 == "y" or question_1 == "yes":
                question = "y"
                print("Please enter another item")
            elif question_1 == "n" or question_1 == "no":
                question = "nope"
                end(totalPrice, task)
            else:
                question = "confirm"
        # Allows the user to add more items or to not add more items




# The end function receives passed variables from the food, drinks or misc function.
# Then shows the user what has been ordered. 
def end(totalPrice, task):
    if task == 1:
        # Prints the food ordered
        print("The item(s) you will receive are: \n")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Food WHERE Quantity >= 1 ")
            items = cursor.fetchall()
        for row in items:
            print(" {0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("The total price of your chosen item(s) is ${0} \n ".format(totalPrice))
        confirm = input("Would you like to order these items? ").lower()
        if confirm == "yes" or confirm == "y":
            # If the order number is #2000, the order is free
            order = randint(1234,9999)
            print("Order number: #{0} ".format(order))
            if order == 2000:
                alt()
            print("Please pay the total of ${0} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(totalPrice, order))
            payment = time.time() + 10800
            # Adds 3 hours to current time (When it has to be paid...)
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\n(In the next 3 hours)")
            print("\nThanks for ordering with 'Sean's Program' ")
        else:
            print("Fair enough, Please use 'Sean's Program' another time. ")
    
    elif task == 2:
        # Prints the drinks ordered
        print("The drink(s) you will receive are: \n")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Drink WHERE Quantity >= 1 ")
            items = cursor.fetchall()
        for row in items:
            print(" {0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("The total price of your chosen drink(s) is ${0} \n ".format(totalPrice))
        # Confirms if the user wants to order the items.
        confirm = input("Would you like to order these items? ").lower()
        if confirm == "yes" or confirm == "y":
            # If the order number is #2000, the order is free
            order = randint(1234,9999)
            print("Order number: #{0} ".format(order))
            if order == 2000:
                alt()
            print("Please pay the total of ${0} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(totalPrice, order))
            payment = time.time() + 10800
            # Adds 3 hours to current time (When it has to be paid...)
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\n(In the next 3 hours)")
            print("\nThanks for ordering with 'Sean's Program' ")
        else:
            print("Fair enough, Please use 'Sean's Program' another time. ")
            
    elif task == 3: 
        # Prints the miscellaneous item data
        print("The item(s) you have chosen are: ")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Other WHERE Quantity >= 1 ")
            items = cursor.fetchall()
        for row in items:
            print(" {0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("The total price of your chosen item(s) is ${0:.2f} \n ".format(round(totalPrice,2)))
        # Confirms if the user wants to order the items.
        confirm = input("Would you like to order these items? ").lower()
        if confirm == "yes" or confirm == "y":
            order = randint(1234,9999)
            # If the order number is #2000, the order is free
            print("\nOrder number: #{0} ".format(order))
            if order == 2000:
                alt()
            print("\nPlease pay the total of ${0:.2f} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(round(totalPrice,2), order))
            payment = time.time() + 10800
            # Adds 3 hours to current time (When it has to be paid...)
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\n(In the next 3 hours)")
            print("\nThanks for ordering with 'Sean's Program' ")
        else:
            print("Fair enough, Please use 'Sean's Program' another time. ")
    reset()
    input("\nPlease press enter to close the program")
# The reset function is called in order to remove the user's entered data from remaining in database for legal reasons. 



# The alt function is present to give the user a chance to get their order without required payment
def alt():
    # Free order if the order number is equal to the number 2000
    print("\nCongratulations this order is free!! ")
    totalPrice = 0
    print("The new and updated total price is $0 \n ")
    print("Thanks for ordering with 'Sean's Program' ")
    reset()
    input("\nPlease press enter to close the program")
    
main()
