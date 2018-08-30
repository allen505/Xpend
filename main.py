
from OCR import final_image

from datetime import datetime as dt

from tkinter import *
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import ttk, messagebox

WINDOW_SIZE="500x300"

global Xpense

class hello:
    def __init__(self):
        self.buttonHeight=20
        self.buttonWidth=50
        self.file1 = open('data.txt', "a")
        self.root = tkinter.Tk()
        self.root.title("Xpend")
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(0,0)
        self.root.iconbitmap(self, default="images\icon2.ico")
        self.mainFrame=Frame(self.root,bg="#15c674")
        self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both",expand=1)
        self.mainp()
        self.root.mainloop()

    def but1fun(self):
        mamt = int(self.entryamt.get())
        mtag = self.entrytag.get()
        time = dt.now()
        text1 = str((mamt, mtag, time))
        self.file1.write(text1)
        self.label2 = Label(self.manualw, text="Transaction is successfully saved.")
        self.label2.grid(row=6, columnspan=3,padx=3,pady=3)
        self.file1.close()
        self.manualw.after(2000, lambda: self.manualw.destroy())

    def manualp(self):
        self.manualw = Tk()
        self.manualw.geometry("500x300")
        Label(self.manualw, text="Enter the amount").grid(row=0,padx=3,pady=3)
        self.entryamt = Entry(self.manualw)
        self.entryamt.grid(row=0, column=1,padx=3,pady=3)
        Label(self.manualw, text="Enter the tag").grid(row=1,padx=3,pady=3)
        self.entrytag = Entry(self.manualw)
        self.entrytag.grid(row=1, column=1,padx=3,pady=3)
        self.bsubmit = ttk.Button(self.manualw, text="Enter into file", command=self.but1fun)
        self.bsubmit.grid(row=4, columnspan=3,padx=3,pady=3)
        # self.bclear=Button(self.manualw,text="Clear contents",command=self.file1.truncate(0))
        # self.bclear.grid(row=5,columnspan=3)
        self.manualw.mainloop()

    def clickp(self):

        file_path = str(askopenfilename(initialdir="images\Sample Bills", title="Select bill image",
                                            filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]))
        final_image(str(file_path))
        #messagebox.showerror("Error","Image was not selected")

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
        self.photo = tkinter.PhotoImage(file="images\logo.gif")
        Label(self.mainFrame,image=self.photo).pack(pady=(0,15))
        self.manualb = ttk.Button(self.mainFrame, text="Enter transaction manually", command=self.manualp)
        self.manualb.pack(padx=3,pady=3)
        self.clickb = ttk.Button(self.mainFrame, text="Enter transaction by picture", command=self.clickp)
        self.clickb.pack(padx=3,pady=3)
        #the following comments are commented out as it belongs to message reading which will be added on in a later build

        #self.msgb = Button(self.root, text="Enter transaction from messages", command=self.msgp)
        #self.msgb.pack()


if __name__ == '__main__':
    hello()
