from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkeys can live up to 300 years')
answer = tkinter.messagebox.askquestion('Question 1', 'Do you like monkeys?')

if answer == 'yes' :
    print('haha')

root.mainloop()