# Menu V0.2
# 10/06/16
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
priceList_2 = [3.99, 3.99, 34.99, 69.00, 8.99, 8.99]
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
        print("Please enter a correct option")
        print("Sending you back to the beginning")
        print("--------------------------------------------------------------")
        main()

def food():
    chosen = []
    print("The current food items available:")
    global itemList
    global priceList
    print("Items available")
    print("{0} ${1},".format(itemList[0], priceList[0]))
    print("{0} ${1},".format(itemList[1], priceList[1]))
    print("{0} ${1},".format(itemList[2], priceList[2]))
    print("{0} ${1},".format(itemList[3], priceList[3]))
    print("{0} ${1},".format(itemList[4], priceList[4]))
    print("{0} ${1}".format(itemList[5], priceList[5]))
    print("Please select one item at a time")
    question_1 = input("What item would you like?")
    question_1 = question_1.lower()
    if question_1 == "fries" or question_1 == "chips":
        chosen.append = itemList[0]
        print(chosen)
         # not working
    
def drinks():
    print("Drinks Function")

def misc():
    print("Misc Function")
    
main()