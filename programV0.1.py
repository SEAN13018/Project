# Menu V0.1 
# 02/06/16
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
def main(): 
    print("Menu Options: 'Food', 'Drinks', 'Own Items'")
    question= input("What would you like to order? ")
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
    print("Food Function")
    
def drinks():
    print("Drinks Function")

def misc():
    print("Misc Function")
    
main()