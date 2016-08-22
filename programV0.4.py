# Menu V0.4
# 22/08/16
# Sean Nichols
# Doesn't run properly in Wing IDE 101 5.0
# USE IDLE 3.5.2

from random import randint

# Global Lists
itemList = ["Fries", "Chicken Burger with Fries", "Pork Burger with Fries", "Vegetable Burger", "Seafood Chowder", "Fish and Chips"]
priceList = [5, 15, 18, 14, 9, 19]
itemList_2 = ["Coca-Cola", "Sprite", "Moet Champagne", "Santana DVX", "Martini", "Pina Colada"]
priceList_2 = [4, 4, 35, 69, 9, 9]
newItems = []
newPrices = []

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
    totalPrice = 0
    quantity = []
    chosen = []  
    if task == 1:
        food(totalPrice, quantity, chosen, task);
    elif task == 2:
        drinks(totalPrice, quantity, chosen, task);
    elif task == 3:
        misc(totalPrice, quantity, chosen, task);
     # Sends correct parameters to functions   
     
def food(totalPrice, quantity, chosen, task):
    global itemList
    global priceList
    question = "y"
    while question == "y" or question == "yes": 
        print("__________________________________________")
        print("The current items selected {0}".format(chosen))   
        print("Total price of your items ${0}\n".format(totalPrice))
        print("The current food items available: ")
        print("{0} ${1}".format(itemList[0], priceList[0]))
        print("{0} ${1}".format(itemList[1], priceList[1]))
        print("{0} ${1}".format(itemList[2], priceList[2]))
        print("{0} ${1}".format(itemList[3], priceList[3]))
        print("{0} ${1}".format(itemList[4], priceList[4]))
        print("{0} ${1}".format(itemList[5], priceList[5]))
        print("__________________________________________")
        print("Please select one item at a time.")
        # Prints the items available for ordering
        question_1 = input("What item would you like? \n ")
        question_1 = question_1.lower()
        
        # Adds the item and quantities to lists. 
        if question_1 == "fries" or question_1 == "chips":
            chosen = [itemList[0]] + chosen
            while question == "y":
                print("\nPlease enter a value between 1 & 15")
                question_2 = input("How many {0} do you want? \n ".format(itemList[0]))
                if question_2.isdigit():
                    question_2 = int(question_2)
                # Quantity must be between 1 and 15
                    if 1 <= question_2 <= 15:
                        quantity.append(question_2)
                        total = quantity[0] * priceList[0]
                        totalPrice = totalPrice + total 
                        print("\nCurrent order total = ${0}".format(totalPrice))
                        question = "x"
                        # If a quantity is not allowed, it will ask for a new quantity
                        
                    elif question_2 == 0:
                        option = input("Would you like to stop entering this item? y/n \n ")
                        option = option.lower()
                        if option == "yes" or option == "y":
            # Need to remove item that isnt wanted... EZ in database. JK Chosen is list...?
                            option = input("Would you like to end this program? y/n \n ")
                            option = option.lower()
                            if option == "yes" or option == "y":
                                question = "A"
                                end(totalPrice, quantity, chosen, task)
                            else:
                                food(totalPrice, quantity, chosen, task)
        # Here 17-08-16 - Not quite working.     Shell - Problem in H
        # Not quite finished...  - Maybe fix other items to look like Fries. 
        # Make other items like fries
                        else:
                            question = "y"
                    # Possibly option for chossing zero as quantity asks to choose item again or choose correct quantity?
                    # returns to top of function?
                    
            
        elif question_1 == "chicken burger" or question_1 == "chicken" or question_1 == "chicken burger with fries":
            chosen = [itemList[1]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0} do you want? ".format(itemList[1])))
                if 1<= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList[1]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "x"

        elif question_1 == "pork burger" or question_1 == "pork" or question_1 == "pork burger with fries":
            chosen = [itemList[2]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0} do you want? ".format(itemList[2])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    print(quantity)
                    total = quantity[0] * priceList[2]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "x"
            
        elif question_1 == "vegetable burger" or question_1 == "vegetable" or question_1 == "vegetables":
            chosen = [itemList[3]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0}(s) do you want? ".format(itemList[3])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList[3]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "x"
            
        elif question_1 == "seafood chowder" or question_1 == "seafood" or question_1 == "chowder":
            chosen = [itemList[4]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How much {0} do you want? ".format(itemList[4])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList[4]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "x"
            
        elif question_1 == "fish and chips" or question_1 == "fish":
            chosen = [itemList[5]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0} do you want? ".format(itemList[5])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList[5]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "x"
            
        else:
            print("\nPlease enter a valid item.")
            food(totalPrice, quantity, chosen, task)
            # Only allows items that are on the list. 

        while question == "x":
            # Make it so it returns them back to the while when entering the wrong thing.
            question = input("Do you want to order more food? yes / no: ")
            question = question.lower()
            # Ignored the no after the second item is entered - FIXED
            if question == "y" or question == "yes":
                question = "z"
                food(totalPrice, quantity, chosen, task)
            elif question == "n" or question == "no":
                question = "z"
                end(totalPrice, quantity, chosen, task)
                # It sends them to the final (end) function
            else:
                # Enters second item, then chooses no - deletes item from list? - FIXED
                # If the user does not want to continue entering items - FIXED                
                print("Please choose a valid option...  y/n ")
                question = "x"

def drinks(totalPrice, quantity, chosen, task):
    global itemList_2
    global priceList_2
    question = "y"
    while question == "y" or question == "yes": 
        print("__________________________________________")
        print("The current drinks selected {0}".format(chosen))   
        print("Total price of your drinks ${0}".format(totalPrice))
        print("The current drinks available: ")
        print("{0} ${1},".format(itemList_2[0], priceList_2[0]))
        print("{0} ${1},".format(itemList_2[1], priceList_2[1]))
        print("{0} ${1},".format(itemList_2[2], priceList_2[2]))
        print("{0} ${1},".format(itemList_2[3], priceList_2[3]))
        print("{0} ${1},".format(itemList_2[4], priceList_2[4]))
        print("{0} ${1}".format(itemList_2[5], priceList_2[5]))
        print("__________________________________________")
        print("Please select one item at a time.")
        question_1 = input("What item would you like? ")
        question_1 = question_1.lower()
        if question_1 == "coca-cola" or question_1 == "coke":
            chosen = [itemList_2[0]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How much {0} do you want? ".format(itemList_2[0])))
                # Quantity must be between 1 and 15
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[0]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
                    # If quantity is not allowed, it will ask for a new quantity
               
        elif question_1 == "sprite": 
            chosen = [itemList_2[1]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How much {0} do you want? ".format(itemList_2[1])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[1]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
    
        elif question_1 == "champagne" or question_1 == "moet" or question_1 == "moet champagne":
            chosen = [itemList_2[2]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0} do you want? ".format(itemList_2[2])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[2]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
                
        elif question_1 == "santana dvx":
            chosen = [itemList_2[3]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0}(s) do you want? ".format(itemList_2[3])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[3]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
                
        elif question_1 == "martini":
            chosen = [itemList_2[4]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How much {0} do you want? ".format(itemList_2[4])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[4]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
                
        elif question_1 == "pina colada": 
            chosen = [itemList_2[5]] + chosen
            while question == "y":
                print("Please enter a value between 1 & 15")
                question_2 = int(input("How many {0} do you want? ".format(itemList_2[5])))
                if 1 <= question_2 <= 15:
                    quantity = [question_2] + quantity
                    total = quantity[0] * priceList_2[5]
                    totalPrice = totalPrice + total 
                    print("Current order total = ${0}".format(totalPrice))
                    question = "PASS"
                
        else:
            print("Please enter a valid item.")
            drinks(totalPrice, quantity, chosen, task)
            # Only allows items that are on the list. 

        question = "x"
        while question == "x":
            # Make it so it returns them back to the while when entering the wrong thing. - WORKING
            question = input("Do you want to order more food? yes / no: \n ")
            question = question.lower()
            if question == "y" or question == "yes":
                question = "z"
                drinks(totalPrice, quantity, chosen, task)
            elif question == "n" or question == "no":
                question = "z"
                end(totalPrice, quantity, chosen, task)
                # It sends them to the final (end) function
                
# Enters second item, then chooses no - deletes item from list? - Fixed
# If the user does not want to continue entering items - Fixed
            else:
                print("Please choose a valid option...  y/n ")
                question = "x"

        
def misc(totalPrice, quantity, chosen, task):
    global newItems
    global newPrices
    question = "y"
    while question == "yes" or question == "y":
        item = input("What is the name of the new item? \n ")
        item = item.capitalize()
# Need to do something to allow it to be added to the start of the list.
# The answer is to use a database
        newItems = [item] + newItems
        price = int(input("What is the price of the item? \n $"))
        # Check for integer / other?
        newPrices = [price] + newPrices
        number = int(input("How many would you like? \n"))
        if 1 <= question_2 <= 15:
            quantity = [number] + quantity
            total = quantity[0] * newPrices[0]
            print("{0} {1}(s) has been added for ${2}".format(quantity[0], newItems[0], total))
            totalPrice = totalPrice + total
            question = input("Would you like to add another item? \n")
            chosen = newItems
            end(totalPrice, quantity, chosen, task)
    # Allows the user to add items with prices
    # Allows the user to choose the items
    
def end(totalPrice, quantity, chosen, task):
    if task == 1:
        # Prints the food data
        print("The total price of your chosen item(s) is ${0} ".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The number of item(s) you will receive is: {0} ".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The item(s) you have chosen are: {0} ".format(chosen_B))
        random = randint(1234,9999)
        print("If your order number is #2000, your order is free. ")
        print("Order number: #{0} ".format(random))
        if random == 2000:
            alt()
        else:
            print("Bad luck, try again next time. ")
            print("Thanks for ordering with 'Sean's Program' ")
    
    elif task == 2:
        # Prints the drink data
        print("The total price of your chosen item(s) is ${0} ".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The quantity of drink(s) you will receive is: {0} ".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The drink(s) you have chosen are: {0} ".format(chosen_B))
        random = randint(1234,9999)
        print("If your order number is #2000, your order is free. ")
        print("Order number: #{0} ".format(random))
        if random == 2000:
            alt()
        else:
            print("Bad luck, try again next time. ")
            print("Thanks for ordering with 'Sean's Program' ")
            
    elif task == 3: 
        # Prints the miscellaneous item data
        print("The total price of your chosen item(s) is ${0} ".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The quantity of item(s) you will receive is: {0} ".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The item(s) you have chosen are: {0} ".format(chosen_B))
        random = randint(1234,9999)
        print("If your order number is #2000, your order is free. ")
        print("Order number: #{0} ".format(random))
        if random == 2000:
            alt()
        else:
            print("Bad luck, try again next time. ")
            print("Thanks for ordering with 'Sean's Program' ")

def alt():
    # Free order if the order number is equal to the number 2000
    print("\nCongratulations this order is free!! ")
    print("The new total price is $0 \n ")
    print("Thanks for ordering with 'Sean's Program' ")
    
main()

# Use database