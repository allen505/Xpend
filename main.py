"""
TO DO:

text_message.py
    recheck all the function and algorithms
    clear the return of the function
    fill in the comments

OCR.py
    check for any missing variables
    ensure proper passing of file_path variable
    ensure proper return or store of data and appropriate message to be displayed

main.py
    ensure uploading of necessary file and file_path for OCR.py
    check for any variable which needs to be passed to the function call
    give a more aesthetic look to the windows
    ensure correct storing a returning of data
    display appropriate error or affirmative messages
    correct the function naming in several instances, for ex: clickp has a collision with one of the OCR packages

"""



from OCR import clickp

from tkinter import *
from datetime import datetime as dt
import tkinter as tk

global Xpend

class hello:
    def __init__(self):
        self.file1 = open('ords.txt', "a")
        self.root = tk.Tk()
        self.root.title("Finance")
        self.mainp()
        self.root.mainloop()

    def but1fun(self):
        mamt = int(self.entryamt.get())
        mtag = self.entrytag.get()
        time = dt.now()
        text1 = str((mamt, mtag, time))
        self.file1.write(text1)
        self.label2 = Label(self.manualw, text="Transaction is successfully saved.")
        self.label2.grid(row=6, columnspan=3)
        self.file1.close()

    def manualp(self):
        self.manualw = Tk()
        label1 = Label(self.manualw, text="Enter the amount").grid(row=0)
        self.entryamt = Entry(self.manualw)
        self.entryamt.grid(row=0, column=1)
        label1 = Label(self.manualw, text="Enter the tag").grid(row=1)
        self.entrytag = Entry(self.manualw)
        self.entrytag.grid(row=1, column=1)
        self.bsubmit = Button(self.manualw, text="Enter into file", command=self.but1fun)
        self.bsubmit.grid(row=4, columnspan=3)
        # self.bclear=Button(self.manualw,text="Clear contents",command=self.file1.truncate(0))
        # self.bclear.grid(row=5,columnspan=3)
        self.manualw.mainloop()

    def clickp(self):
        self.clickw = Tk()
        pass
        self.clickw.mainloop()

    def msgp(self):
        self.msgp = Tk()
        pass
        self.msgp.mainloop()

    def mainp(self):
        self.manualb = Button(self.root, text="Enter transaction manually", command=self.manualp)
        self.manualb.pack()
        self.clickb = Button(self.root, text="Enter transaction by picture", command=self.clickp)
        self.clickb.pack()
        self.msgb = Button(self.root, text="Enter transaction from messages", command=self.msgp)
        self.msgb.pack()


if __name__ == '__main__':
    hello()
