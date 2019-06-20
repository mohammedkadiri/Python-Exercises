from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()
bot_frame = Frame(root)
bot_frame.pack(side=BOTTOM)

btn_one = Button(top_frame, text="Button 1", fg="red")
btn_two = Button(top_frame, text="Button 2", fg="blue")
btn_three = Button(top_frame, text="Button 3", fg="green")
btn_four = Button(bot_frame, text="Button 4", fg="purple")

btn_one.pack(side=LEFT)
btn_two.pack(side=LEFT)
btn_three.pack(side=LEFT)
btn_four.pack(side=BOTTOM)

root.mainloop()