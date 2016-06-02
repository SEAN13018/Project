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

