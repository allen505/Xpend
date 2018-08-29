
from OCR import final_image

from datetime import datetime as dt

from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import ttk, messagebox

global Xpend

class hello:
    def __init__(self):
        self.buttonHeight=20
        self.buttonWidth=50
        self.file1 = open('ords.txt', "a")
        self.root = tkinter.Tk("Xpend")
        self.root.geometry("500x300")
        #this makes the main window
        #self.root.title("")
        self.root.iconbitmap(self, default="images\icon.ico")
        self.topFrame=Frame(self.root)
        self.topFrame.pack()
        self.bottomFrame=Frame(self.root)
        self.bottomFrame.pack(side="bottom")
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
        self.manualw.geometry("500x300")
        Label(self.manualw, text="Enter the amount").grid(row=0)
        self.entryamt = Entry(self.manualw)
        self.entryamt.grid(row=0, column=1)
        Label(self.manualw, text="Enter the tag").grid(row=1)
        self.entrytag = Entry(self.manualw)
        self.entrytag.grid(row=1, column=1)
        self.bsubmit = ttk.Button(self.manualw, text="Enter into file", command=self.but1fun)
        self.bsubmit.grid(row=4, columnspan=3)
        # self.bclear=Button(self.manualw,text="Clear contents",command=self.file1.truncate(0))
        # self.bclear.grid(row=5,columnspan=3)
        self.manualw.mainloop()

    def clickp(self):
        try:
            file_path = str(askopenfilename(initialdir="images\Sample Bills", title="Select bill image",
                                            filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]))
            final_image(str(file_path))
        except:
            messagebox.showerror("Error","Image was not selected")

        """
        amt=final_image(str(file_path))
        label=Label(self.mainp,text=amt).grid(row=0)
        label.pack()
        """




    def msgp(self):
        #this functions will be improvied in a later build
        self.msgp = Tk()
        pass
        self.msgp.mainloop()

    def mainp(self):
        #this is the first window which displays as soon as the program runs
        self.manualb = ttk.Button(self.root, text="Enter transaction manually", command=self.manualp)
        self.manualb.pack()
        self.clickb = ttk.Button(self.root, text="Enter transaction by picture", command=self.clickp)
        self.clickb.pack()
        #the following comments are commented out as it belongs to message reading which will be added on in a later build

        #self.msgb = Button(self.root, text="Enter transaction from messages", command=self.msgp)
        #self.msgb.pack()


if __name__ == '__main__':
    hello()
