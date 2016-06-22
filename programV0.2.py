# Menu V0.2
# 23/06/16
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

# Tkinter not incorporated at this stage 9/6/16

# Global Lists
itemList = ["Fries", "Chicken Burger with Fries", "Pork Burger with Fries", "Vegetable Burger", "Seafood Chowder", "Fish and Chips"]
priceList = [5, 15, 18, 14, 9, 19]
itemList_2 = ["Coca-Cola", "Sprite", "Moet Champagne", "Santana DVX", "Martini", "Pina Colada"]
priceList_2 = [4, 4, 35, 69, 9, 9]
newItems = []
newPrices = []


def main():
    print("Menu Options: 'Food', 'Drinks', 'Own Items'")
    question = input("What would you like to order? :")
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
        print("--------------------------------------------------------------")
        main()
def setup(task):
    totalPrice = 0
    quantity = []
    chosen = []  
    if task == 1:
        food(totalPrice, quantity, chosen);
    elif task == 2:
        drinks(totalPrice, quantity, chosen);
        
def food(totalPrice, quantity, chosen):
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
        question_1 = input("What item would you like? ")
        question_1 = question_1.lower()
        if question_1 == "fries" or question_1 == "chips":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[0])))
            quantity.append(question_2)
            total = quantity[0] * priceList[0]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "chicken burger" or question_1 == "chicken" or question_1 == "chicken burger with fries":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[1])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[1]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))  

        elif question_1 == "pork burger" or question_1 == "pork" or question_1 == "pork burger with fries":
            chosen = [question_1] + chosen
            chosen.append(itemList[2])
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[2])))
            quantity = [question_2] + quantity
            print(quantity)
            total = quantity[0] * priceList[2]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "vegetable burger" or question_1 == "vegetable" or question_1 == "vegetables":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0}(s) do you want? Enter a value between 1 & 15: ".format(itemList[3])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[3]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "seafood chowder" or question_1 == "seafood" or question_1 == "chowder":
            chosen = [question_1] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList[4])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[4]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        elif question_1 == "fish and chips" or question_1 == "fish":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[5])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[5]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
            
        else:
            print("Please enter a valid item.")
            food(totalPrice, quantity, chosen);
            
        question = input("Do you want to order more food? yes / no: ")
        question = question.lower()
        if question == "n" or question == "no":
            print("The total price of your chosen items is ${0}".format(totalPrice))
            print("The total items of food you will receive is {0}".format(quantity))
            print("The items you have chosen are: {0}".format(chosen))
            end(totalPrice, quantity, chosen) 
            
# drinks - not the correct lists or items

def drinks(totalPrice, quantity, chosen):
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
            chosen = [question_1] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList[0])))
            quantity.append(question_2)
            total = quantity[0] * priceList[0]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
# 23-06-16 Up to here changing names                
        elif question_1 == "sprite": 
            chosen = [question_1] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList[1])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[1]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))  
    
        elif question_1 == "pork burger" or question_1 == "pork" or question_1 == "pork burger with fries":
            chosen = [question_1] + chosen
            chosen.append(itemList[2])
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[2])))
            quantity = [question_2] + quantity
            print(quantity)
            total = quantity[0] * priceList[2]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "vegetable burger" or question_1 == "vegetable" or question_1 == "vegetables":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0}(s) do you want? Enter a value between 1 & 15: ".format(itemList[3])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[3]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "seafood chowder" or question_1 == "seafood" or question_1 == "chowder":
            chosen = [question_1] + chosen
            question_2 = int(input("How much {0} do you want? Enter a value between 1 & 15: ".format(itemList[4])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[4]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        elif question_1 == "fish and chips" or question_1 == "fish":
            chosen = [question_1] + chosen
            question_2 = int(input("How many {0} do you want? Enter a value between 1 & 15: ".format(itemList[5])))
            quantity = [question_2] + quantity
            total = quantity[0] * priceList[5]
            totalPrice = totalPrice + total 
            print("Current order total = ${0}".format(totalPrice))
                
        else:
            print("Please enter a valid item.")
            food(totalPrice, quantity, chosen);
                
        question = input("Do you want to order more food? yes / no: ")
        question = question.lower()
        if question == "n" or question == "no":
            print("The total price of your chosen items is ${0}".format(totalPrice))
            print("The total items of food you will receive is {0}".format(quantity))
            print("The items you have chosen are: {0}".format(chosen))
            end(totalPrice, quantity, chosen)     
        
def misc():
    print("Misc Function")
    
def end(totalPrice, quantity, chosen):
    print("End function")
    
main()
