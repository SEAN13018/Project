# Menu V0.5
# 20/09/16
# Sean Nichols
# Runs best with IDLE 3.5.2

from random import randint
import sqlite3
import string
import itertools
import time 

def reset():
    with sqlite3.connect("project_Database.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE Food SET Quantity = 0")
        cursor.execute("UPDATE Drink SET Quantity = 0")
        cursor.execute("DELETE FROM Other")
        # Resets the data entered by the user.

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

# Function asks and directs person to the next function that they require. 
def main():
    print("Welcome to Sean's Program: Menu V0.4 \n")
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
        # Sends the user to the correct function
        
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
     
def food(totalPrice, task):
    global itemList
    global priceList
    question = "y"
    while question == "y" or question == "yes": 
        print("_____________________________________________")  
        print("Total price of your items ${0}\n".format(totalPrice))
        print("The current food items available: \n")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Food")
            items = cursor.fetchall()
        for row in items:
            print("{0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("Please select one item at a time.")
        # Prints the items available for ordering
        question_1 = input("What item would you like? \n ").lower()
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price FROM Food WHERE Name_lower = '{0}'".format(question_1))
            check = cursor.fetchall()
            # Checks if there is an item called "What the user wants"
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
            # Enters second item, then chooses no - deletes item from list? - FIXED
            # If the user does not want to continue entering items - FIXED                
            print("Please choose a valid option...  y/n ")
            question = "x"

def drinks(totalPrice, task):
    # Input not registering 14/09/16 - Need to fix
    global itemList_2
    global priceList_2
    question = "y"
    while question == "y" or question == "yes": 
        print("_____________________________________________")  
        print("Total price of your items ${0}\n".format(totalPrice))
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
            # Checks if there is an drink called "What the user wants"
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
        print("Please enter one item at a time.")
        item = input("What is the name of the new item? \n ").capitalize()
        true = "true"
        while true == "true":
            price = float(input("What is the price of the item? \n $"))
            if isinstance(price, float):
                true = "a"
        while true == "a":
            quantity = int(input("How many would you like? \n"))
            if 1 <= quantity <= 15:
                total = quantity * price
                true = "b"
            else:
                print("Please enter a quantity between 1 and 15. ")
        new = item, price, quantity
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
        # Allows the user to add items with prices
    
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
        print("If your order number is #2000, your order is free. ")
        order = randint(1234,9999)
        print("Order number: #{0} ".format(order))
        if order == 2000:
            alt()
        else:
            print("\nBad luck, try again next time. ")
            print("Please pay the total of ${0} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(totalPrice, order))
            payment = time.time() + 601200
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\nThanks for ordering with 'Sean's Program' ")
    
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
        print("If your order number is #2000, your order is free. ")
        order = randint(1234,9999)
        print("Order number: #{0} ".format(order))
        if order == 2000:
            alt()
        else:
            print("\nBad luck, try again next time. ")
            print("Please pay the total of ${0} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(totalPrice, order))
            payment = time.time() + 601200
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\nThanks for ordering with 'Sean's Program' ")
            
    elif task == 3: 
        # Prints the miscellaneous item data
        print("The item(s) you have chosen are: {0} ")
        with sqlite3.connect("project_Database.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT Name, Price, Quantity FROM Other WHERE Quantity >= 1 ")
            items = cursor.fetchall()
        for row in items:
            print(" {0}  ${1}, Quantity:{2}".format(row[0], row[1], row[2]))
        print("\n")
        print("The total price of your chosen item(s) is ${0} \n ".format(totalPrice))
        order = randint(1234,9999)
        print("If your order number is #2000, your order is free. ")
        print("Order number: #{0} ".format(order))
        if order == 2000:
            alt()
        else:
            print("\nBad luck, try again next time. ")
            print("Please pay the total of ${0} to the account 1234-5678-9012-34 \nwith the order number, #{1} as the reference.".format(totalPrice, order))
            payment = time.time() + 601200
            print("Payment by {0} is appreciated. ".format(time.ctime(payment)))
            print("\nThanks for ordering with 'Sean's Program' ")

def alt():
    # Free order if the order number is equal to the number 2000
    print("\nCongratulations this order is free!! ")
    print("The new total price is $0 \n ")
    print("Thanks for ordering with Sean's Program ")
    
main()
