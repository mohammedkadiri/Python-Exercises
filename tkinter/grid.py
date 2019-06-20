from tkinter import *

root = Tk()

lab_1 = Label(root, text="Name")
lab_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

lab_1.grid(row=0)
lab_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

root.mainloop()