from tkinter import *
from math import *


def lahenda():
    if (a.get()!=""and b.get()!=""and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=(-1*b_+sqrt(D))/(2*a_)
            x2_=(-1*b_-sqrt(D))/(2*a_)
            t=f"x1{x1_},\nx2={x2_}"
        elif D==0:
            x1_=(-1*b_)/(2*a_)
            t=f"x1={x1_}"
        else: 
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
    else:
        if a.get()=="":
            a.configure(bg="yellow")
        elif b.get()=="":
            b.configure(bg="yellow")
        elif c.get()=="":
            c.configure(bg="yellow")

aken=Tk()
aken.geometry("600x600")

lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="red",bg="black")
lbl.pack()
vastus=Label(aken, height=4,width=20,fg="red",bg="lightblue")
vastus.pack(side=BOTTOM)
a=Entry(aken,font="Calibri 26", fg="red",bg="blue",width=3)
a.pack(side=LEFT)
x2=Label(aken,text="x**2+",font="Calibri 26", fg="green")
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26", fg="red",bg="blue",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26", fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Calibri 26", fg="red",bg="blue",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26", fg="green")
y.pack(side=LEFT)

btn=Button(aken,text="Решить",font="Calibri 26", fg="brown",command=lahenda)
btn.pack(side=LEFT)



aken.mainloop()
