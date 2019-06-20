from tkinter import *

root = Tk()

photo = PhotoImage(file="mo.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()