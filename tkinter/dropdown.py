from tkinter import *

def doNothing():
    print("ok i won't")

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

root.mainloop()
