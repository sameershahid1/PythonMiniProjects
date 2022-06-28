from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox


class Hosptal:
    def __init__(self,root):
        self.root=root
        self.root.title("Hoipital Mangement System")
        self.root.geometry("1540x800+0+0")
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSIPTAL MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))

root=Tk()
ob=Hosptal(root)
root.mainloop()