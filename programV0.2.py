# Menu V0.2
# 16/06/16
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
#Tkinter not finished

#Tkinter not incorporated at this stage 9/6/16

#Global Lists
itemList = ["Fries", "Chicken Burger with Fries", "Pork Burger with Fries", "Vegetable Burger", "Seafood Chowder", "Fish and Chips"]
priceList = [4.99, 14.99, 17.99, 13.99, 8.99, 18.99]
itemList_2 = ["Coca-Cola", "Sprite", "Moet Champagne", "Santana DVX", "Martini", "Pina Colada"]
priceList_2 = [3.99, 3.99, 34.99, 69, 8.99, 8.99]
newItems = []
newPrices = []
    
def main(): 
    print("Menu Options: 'Food', 'Drinks', 'Own Items'")
    question= input("What would you like to order? :")
    question = question.lower()
    if question == "food":
        food()
    elif question == "drinks" or question == "drink":
        drinks()
    elif question == "own items" or question == "own" or question == "own item": 
        misc()
    else:
        print("Please enter a valid option")
        print("Sending you back to the beginning")
        print("--------------------------------------------------------------")
        main()

def food():
    quantity= []
    # while  - here to order different items 
    question = input("Do you want to order food? ")
    question = question.lower()
    if question == "n" or question == "no":
        end(totalPrice, quantity, chosen)
    print("The current items selected {0}".format(chosen))    
    print("The current food items available: ")
    global itemList
    global priceList
    print("{0} ${1},".format(itemList[0], priceList[0]))
    print("{0} ${1},".format(itemList[1], priceList[1]))
    print("{0} ${1},".format(itemList[2], priceList[2]))
    print("{0} ${1},".format(itemList[3], priceList[3]))
    print("{0} ${1},".format(itemList[4], priceList[4]))
    print("{0} ${1}".format(itemList[5], priceList[5]))
    print("Please select one item at a time.")
    question_1 = input("What item would you like? ")
    question_1 = question_1.lower()
    if question_1 == "fries" or question_1 == "chips":
        chosen.append(itemList[0])
        question_2 = int(input("How many {0}(s) do you want? Enter a value between 1 & 15: ".format(chosen)))
        quantity.append(question_2)
    # doing stuff here 2:38 16-06-16
def drinks():
    global itemList_2
    global priceList_2
    chosen = []
    print("The current food items available:")
    print("{0} ${1},".format(itemList_2[0], priceList_2[0]))
    print("{0} ${1},".format(itemList_2[1], priceList_2[1]))
    print("{0} ${1},".format(itemList_2[2], priceList_2[2]))
    print("{0} ${1},".format(itemList_2[3], priceList_2[3]))
    print("{0} ${1},".format(itemList_2[4], priceList_2[4]))
    print("{0} ${1}".format(itemList_2[5], priceList_2[5]))
    print("Please select one item at a time. ")
    question_1 = input("What item would you like? ")
    question_1 = question_1.lower()
    if question_1 == "coke" or question_1 == "coca cola" or question_1 == "coca-cola" or question_1 == "cola":
        chosen.append(itemList_2[0])
        print(chosen)
    
        
def misc():
    print("Misc Function")
    
main()
