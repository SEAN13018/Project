# Menu V0.3
# 01/07/16
# Sean Nichols

from tkinter import *
GUI = Tk()
GUI.geometry("680x500")
GUI.title("Menu Program")
topFrame = Frame(GUI)
topFrame.pack()
bottomFrame = Frame(GUI)
bottomFrame.pack(side=BOTTOM)
GUI.configure(background='light blue')

menu = Menu(GUI)
GUI.config(menu=menu)
subMenu = Menu(menu)
# Tkinter not finished
# Use lynda.com

# Tkinter not incorporated at this stage 9/6/16

from random import randint

# Global Lists
itemList = ["Fries", "Chicken Burger with Fries", "Pork Burger with Fries", "Vegetable Burger", "Seafood Chowder", "Fish and Chips"]
priceList = [5, 15, 18, 14, 9, 19]
itemList_2 = ["Coca-Cola", "Sprite", "Moet Champagne", "Santana DVX", "Martini", "Pina Colada"]
priceList_2 = [4, 4, 35, 69, 9, 9]
newItems = []
newPrices = []

def main():
    print("Menu Options: 'Food', 'Drinks', 'Own Items'")
    question = input("What would you like to order? : ")
    question = question.lower()
    if question == "food":
        task = 1
        setup(task);
    elif question == "drinks" or question == "drink":
        task = 2
        setup(task)
    elif question == "own items" or question == "own" or question == "own item": 
        misc()
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
    question = "y"
    while question == "y" or question == "yes": 
        print("__________________________________________")
        print("The current items selected {0}".format(chosen))   
        print("Total price of your items ${0}".format(totalPrice))
        print("The current food items available: ")
        global itemList
        global priceList
        print("{0} ${1},".format(itemList[0], priceList[0]))
        print("{0} ${1},".format(itemList[1], priceList[1]))
        print("{0} ${1},".format(itemList[2], priceList[2]))
        print("{0} ${1},".format(itemList[3], priceList[3]))
        print("{0} ${1},".format(itemList[4], priceList[4]))
        print("{0} ${1}".format(itemList[5], priceList[5]))
        print("__________________________________________")
        print("Please select one item at a time.")
        # Prints the items available for ordering
        question_1 = input("What item would you like? ")
        question_1 = question_1.lower()
        # Adds the item and quantities to lists. 
        if question_1 == "fries" or question_1 == "chips":
            chosen = [itemList[0]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[0])))
            # Needs limit on quantity for all. Note on tkinter and as a note on the program
            quantity.append(question_2)
            total = quantity[0] * priceList[0]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "chicken burger" or question_1 == "chicken" or question_1 == "chicken burger with fries":
            chosen = [itemList[1]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[1])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[1]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))  

        elif question_1 == "pork burger" or question_1 == "pork" or question_1 == "pork burger with fries":
            chosen = [itemList[2]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[2])))
            quantity = [question_2] + quantity
            print(quantity)
            total = quantity[0] * priceList[2]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "vegetable burger" or question_1 == "vegetable" or question_1 == "vegetables":
            chosen = [itemList[3]] + chosen
            question_2 = int(input("How many {0}(s) do you want? Enter a value between 1 & 15: ".format(itemList[3])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[3]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "seafood chowder" or question_1 == "seafood" or question_1 == "chowder":
            chosen = [itemList[4]] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList[4])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[4]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "fish and chips" or question_1 == "fish":
            chosen = [itemList[5]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[5])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[5]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        else:
            print("Please enter a valid item.")
            food(totalPrice, quantity, chosen, task)
            # Only allows items that are on the list. 

        question = "x"
        while question == "x":
            # Make it so it returns them back to the while when entering the wrong thing.
            question = input("Do you want to order more food? yes / no: ")
            question = question.lower()
            # Ignores the no after the second item is entered 1:27 1/7/16
            if question == "y" or question == "yes":
                food(totalPrice, quantity, chosen, task)
            elif question == "n" or question == "no":
                end(totalPrice, quantity, chosen, task)
                #If the user does not want to continue entering items
                # it sends them to the final (end) function
            else:
                print("Please choose a valid option...  y/n ")
                question = "x"

def drinks(totalPrice, quantity, chosen, task):
    question = "y"
    while question == "y" or question == "yes": 
        print("__________________________________________")
        print("The current drinks selected {0}".format(chosen))   
        print("Total price of your drinks ${0}".format(totalPrice))
        print("The current drinks available: ")
        global itemList_2
        global priceList_2
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
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList_2[0])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList_2[0]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
               
        elif question_1 == "sprite": 
            chosen = [itemList_2[1]] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList_2[1])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList_2[1]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))  
    
        elif question_1 == "champagne" or question_1 == "moet" or question_1 == "moet champagne":
            chosen = [itemList_2[2]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList_2[2])))
            quantity = [question_2] + quantity
            print(quantity)
            total = quantity[0] * priceList_2[2]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "santana dvx":
            chosen = [itemList_2[3]] + chosen
            question_2 = int(input("How many {0}(s) do you want? Enter a value between 1 & 15: ".format(itemList_2[3])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList_2[3]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "martini":
            chosen = [itemList_2[4]] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList_2[4])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList_2[4]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "pina colada": 
            chosen = [itemList_2[5]] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList_2[5])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList_2[5]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        else:
            print("Please enter a valid item.")
            food(totalPrice, quantity, chosen, task);
            # Returns to the start of the food function with the user's 
            # previous choices   
        false = 1
        while false == 1:
            question = input("Do you want to order more food? yes / no: ")
            question = question.lower()
            if question == "y" or question == "yes":
                drinks(totalPrice, quantity, chosen, task)
                false = 0
            elif question == "n" or question == "no":
                end(totalPrice, quantity, chosen, task)
                false = 0
            else:
                print("Please choose a valid option...  y/n ")
                false = 1
                #If the user does not want to continue entering items
                # it sends them to the final (end) function
        
def misc(totalPrice, quantity, chosen, task):
    global newItems
    global newPrices
    # Allow user to add items with prices
    # Allow user to choose the items
    
def end(totalPrice, quantity, chosen, task):
    if task == 1:
        # Prints the food data
        print("The total price of your chosen items is ${0}".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The number of items you will receive is: {0}".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The items you have chosen are: {0}".format(chosen_B))
         
    elif task == 2:
        # Prints the drink data
        print("The total price of your chosen items is ${0}".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The quantity of drinks you will receive is: {0}".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The drinks you have chosen are: {0}".format(chosen_B))
        random = randint(1234,9999)
        random = 2000
        if random == 2000:
            alt()
        else:
            print("Welcome to the end of the beginning")
            

    elif task == 3: 
        # Prints the miscellaneous item data
        print("The total price of your chosen items is ${0}".format(totalPrice))
        sum_quantity = sum(quantity)
        print("The quantity of items you will receive is: {0}".format(sum_quantity))
        chosen_B = chosen[::-1]
        print("The items you have chosen are: {0}".format(chosen_B))

def alt():
    print("Congratulations this order is free!!")
    totalPrice = 0
    print("The new total price is ${0}".format(totalPrice))
    print(".")
    print(".")
    print(".")
    print("Thanks for ordering with Sean")
main()
