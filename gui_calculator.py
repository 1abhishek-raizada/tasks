
import tkinter as tk
from tkinter import *

#used for creating gui
root=tk.Tk()
root.geometry('460x150')
root.title('Simple Calculator')
root.configure(bg='#a7adba')
def div():
    x=float(name1.get())
    y=float(name2.get())
    c=x/y 
    result.set(f"{c}")
def mult():
    x=float(name1.get())
    y=float(name2.get())
    c=x*y 
    result.set(f"{c}")
def sub():
    x=float(name1.get())
    y=float(name2.get())
    c=x-y 
    result.set(f"{c}")
def add():
    x=float(name1.get())
    y=float(name2.get())
    c=x+y
    result.set(f"{c}")

heading=Label(root,text='Simple calculator',bg='#a7adba')    
heading.grid(row=0,column=0,columnspan=3)

slot1=Label(root,text='Enter the irst number:',bg='#a7adba')
slot1.grid(row=1,column=0)
name1=Entry(root,border=5)
name1.grid(row=1,column=1)
slot2=Label(root,text='Enter the Second number:',bg='#a7adba')
slot2.grid(row=2,column=0)
name2=Entry(root,border=5)
name2.grid(row=2,column=1)

bt=Button(root,text='+',font=(11),height=1,width=3,command=add,bg='#c0c5ce')
bt.grid(row=1,column=5,columnspan=1)
bt2=Button(root,text='-',font=(11),height=1,width=3,command=sub,bg='#c0c5ce')
bt2.grid(row=1,column=6,columnspan=1)
bt3=Button(root,text='x',height=1,width=3,command=mult,bg='#c0c5ce')
bt3.grid(row=2,column=5,columnspan=1)
bt4=Button(root,text='÷',font=(11),height=1,width=3,command=div,bg='#c0c5ce')
bt4.grid(row=2,column=6,columnspan=1)


slot3=Label(root,text='Answer is:',bg='#a7adba')
slot3.grid(row=4,column=0)
result=StringVar()
result.set("")
result_slot=Entry(root,textvariable=result,state='readonly',border=5)

result_slot.grid(row=4, column=1, columnspan=3, pady=10)

root.mainloop()