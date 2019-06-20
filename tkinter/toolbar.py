from tkinter import *

def doNothing():
    print("ok i won't")

# ***** main menu *****

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_separator()

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)

# ***** Toolbar ****
toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert image", command=doNothing)
insertButt.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)

# ***** Status bar ****
status = Label(root, text="Prepare to do nothing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
