from tkinter import *


class MoButton:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printBtn = Button(frame, text="Print message", command=self.printMessage)
        self.printBtn.pack(side=LEFT)

        self.quitBtn = Button(frame, text="Quit", command=frame.quit)
        self.quitBtn.pack(side=LEFT)

    def printMessage(self):
        print("Wow, it works")


root = Tk()
b = MoButton(root)
root.mainloop()