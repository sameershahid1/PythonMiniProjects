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
        self.root.geometry("1024x768+0+0")
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSIPTAL MANAGMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
    
        #====================================Data Frame=====================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1360,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=840,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=850,y=5,width=460,height=350)
        
        #===================================Button=======================================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1360,height=70)

        #===================================Details=============================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1360,height=100)


root=Tk()
ob=Hosptal(root)
root.mainloop()

