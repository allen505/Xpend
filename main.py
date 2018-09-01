
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
        self.root.config(background="#fcfffb")
        self.root.iconbitmap(self, default="images\icon2.ico")

        self.photoFrame=Frame(self.root,bg="#fcfffb").grid(row=0)
        #self.photoFrame.pack_propagate(0)
        #self.photoFrame.pack(fill="both",expand=1)
        self.mainFrame=Frame(self.root,bg="#15c674").grid(row=1)
        #self.mainFrame.pack_propagate(0)
        #self.mainFrame.pack(fill="both",expand=1)
        self.manualFrame = Frame(self.root, bg="#15c674").grid(row=1)
        #self.manualFrame.pack_propagate(0)
        #self.manualFrame.pack(fill="both", expand=1)

        self.mainp()
        self.root.mainloop()

    def but1fun(self):
        mamt = int(self.entryamt.get())
        mtag = self.entrytag.get()
        time = dt.now()
        text1 = str((mamt, mtag, time))
        self.file1.write(text1)
        self.label2 = Label(self.manualFrame, text="Transaction is successfully saved.")
        self.label2.grid(row=6, columnspan=3,padx=3,pady=3)
        self.file1.close()


    def manualp(self):
        self.manualFrame.tkraise()
        Label(self.manualFrame, text="Enter the amount").grid(row=0,padx=3,pady=3)
        self.entryamt = Entry(self.manualFrame)
        self.entryamt.grid(row=0, column=1,padx=3,pady=3)
        Label(self.manualFrame, text="Enter the tag").grid(row=1,padx=3,pady=3)
        self.entrytag = Entry(self.manualFrame)
        self.entrytag.grid(row=1, column=1,padx=3,pady=3)
        self.bsubmit = ttk.Button(self.manualFrame, text="Enter into file", command=self.but1fun).grid(row=4, columnspan=3,padx=3,pady=3)
        ttk.Button(self.mainFrame, text="Go back to home", command=lambda: self.mainFrame.tkraise()).grid(row=5, columnspan=3,padx=3,pady=3)
        # self.bclear=Button(self.manualFrame,text="Clear contents",command=self.file1.truncate(0))
        # self.bclear.grid(row=5,columnspan=3)

    def clickp(self):

        file_path = str(askopenfilename(initialdir="images\Sample Bills", title="Select bill image",
                                            filetypes=[("Image Files", "*.jpeg;*.jpg;*.png")]))
        final_image(str(file_path))
        #messagebox.showerror("Error","Image was not selected")


    def msgp(self):
        #this functions will be improvied in a later build
        self.msgp = Tk()
        pass
        self.msgp.mainloop()

    def mainp(self):
        #this is the first window which displays as soon as the program runs
        #self.mainFrame.tkraise()
        self.photo = tkinter.PhotoImage(file="images\logo.gif")
        Label(self.photoFrame,image=self.photo).grid()
        self.manualb = ttk.Button(self.mainFrame, text="Enter transaction manually", command=self.manualp).grid(padx=3,pady=(3,0))
        self.clickb = ttk.Button(self.mainFrame, text="Enter transaction by picture", command=self.clickp).grid(padx=3,pady=3)


if __name__ == '__main__':
    hello()
