from tkinter import *

root = Tk()

def print_name(event):
    print("Hello my name is Mo")

btn1 = Button(root, text="Print my name")
btn1.bind("<Button-1>", print_name)
btn1.pack()
root.mainloop()