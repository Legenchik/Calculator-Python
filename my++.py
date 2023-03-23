from tkinter import*
tk=Tk()
tk.title("Калькулятор")
tk.config(bg="#808000")
tk.geometry("260x430")
ent=Entry(font="14",justify="right")
ent.config(bg="#800000")
ent.place(x=20,y=20,width=220,height=30)
from math import*
#змінні
#x3
def x3_click():
    a=float(ent.get())
    ent.delete(0,END)
    w=a*a*a
    y=result(w)

x3=Button(text="1",font="14",background="#006400",foreground="#FFFF00",command=x3_click)
x3.place(x=200,y=70,width=40,height=40)
#x2
def x2_click():
    a=float(ent.get())
    ent.delete(0,END)
    w=a*a
    y=result(w)

x2=Button(text="2",font="14",background="#006400",foreground="#FFFF00",command=x2_click)
x2.place(x=140,y=70,width=40,height=40)
#Hi
def Hi_click():
    global a,b
    a=float(ent.get())
    b="1"
    ent.delete(0,END)
Hi=Button(text="Hi",font="14",background="#006400",foreground="#FFFF00",command=Hi_click)
Hi.place(x=80,y=70,width=40,height=40)
#pi
def Pi_click():
    ent.insert(END,"3.14")
Pi=Button(text="pi",font="14",background="#006400",foreground="#FFFF00",command=Pi_click)
Pi.place(x=20,y=70,width=40,height=40)
#/
def Divide_click():
    global a,b
    a=float(ent.get())
    b="/"
    ent.delete(0,END)
Divide=Button(text="/",font="14",background="#006400",foreground="#FFFF00",command=Divide_click)      
Divide.place(x=200,y=190,width=40,height=40)
#*
def Multiply_click():
    global a,b
    a=float(ent.get())
    b="*"
    ent.delete(0,END)
Multiply=Button(text="*",font="14",background="#006400",foreground="#FFFF00",command=Multiply_click)
Multiply.place(x=200,y=250,width=40,height=40)
#-
def Minus_click():
    global a,b
    if ent.get()=="":
        ent.insert(END,"-")
    else:
        a=float(ent.get())
        b="-"
        ent.delete(0,END)
Minus=Button(text="-",font="14",background="#006400",foreground="#FFFF00",command=Minus_click)
Minus.place(x=200,y=310,width=40,height=40)
#+
def Plus_click():
    global a,b
    a=float(ent.get())
    b="+"
    ent.delete(0,END)
Plus=Button(text="+",font="14",background="#006400",foreground="#FFFF00",command=Plus_click)
Plus.place(x=200,y=370,width=40,height=40)
#c
def BC_click():
    ent.delete(0,END)
BC=Button(text="c",font="14",background="#006400",foreground="#FFFF00",command=BC_click)
BC.place(x=20,y=130,width=40,height=40)
#=
def result(w):
    if w==int(w):
        ent.insert(END,int(w))
    else:
        ent.insert(END,w)
def Equal_click():
    global w,a
    c=float(ent.get())
    ent.delete(0,END)
    if b=="+":
        w=a+c
        y=result(w)
    if b=="-":
        w=a-c
        y=result(w)
    if b=="*":
        w=a*c
        y=result(w)
    if b=="/":
        if c!=0:
            w=a/c
            y=result(w)
        else:
            ent.insert(END,"помилка")
    if b=="1":
        w=hypot(a,c)
        y=result(w)
Equal=Button(text="=",font="14",background="#006400",foreground="#FFFF00",command=Equal_click)
Equal.place(x=200,y=130,width=40,height=40)
#.
def Point_click():
    ent.insert(END,".")
Point=Button(text=".",font="14",background="#006400",foreground="#FFFF00",command=Point_click)
Point.place(x=140,y=370,width=40,height=40)
#radical
def Radical_click():
    a=float(ent.get())
    ent.delete(0,END)
    if a>=0:
        w=sqrt(a)
        y=result(w)
    else:
        ent.insert(END,"помилка!!!!!!!!!!!!!!!!!!!!")

Radical=Button()
Radical=Button(text="3",background="#006400",foreground="#FFFF00",command=Radical_click)
Radical.place(x=80,y=130,width=40,height=40)
#Modul
def Modul_click():
    a=float(ent.get())
    ent.delete(0,END)
    w=abs(a)
    y=result(w)
Modul=Button(text="|x|",font="14",background="#006400",foreground="#FFFF00",command=Modul_click)
Modul.place(x=140,y=130,width=40,height=40)
#9
def B9_click():
    ent.insert(END,"9")
B9=Button(text="9",font="14",background="#00FFFF",command=B9_click)
B9.place(x=140,y=190,width=40,height=40)
#8
def B8_click():
    ent.insert(END,"8")
B8=Button(text="8",font="14",background="#00FFFF",command=B8_click)
B8.place(x=80,y=190,width=40,height=40)
#7
def B7_click():
    ent.insert(END,"7")
B7=Button(text="7",font="14",background="#00FFFF",command=B7_click)
B7.place(x=20,y=190,width=40,height=40)
#6
def B6_click():
    ent.insert(END,"6")
B6=Button(text="6",font="14",background="#00FFFF",command=B6_click)
B6.place(x=140,y=250,width=40,height=40)
#5
def B5_click():
    ent.insert(END,"5")
B5=Button(text="5",font="14",background="#00FFFF",command=B5_click)
B5.place(x=80,y=250,width=40,height=40)
#4
def B4_click():
    ent.insert(END,"4")
B4=Button(text="4",font="14",background="#00FFFF",command=B4_click)
B4.place(x=20,y=250,width=40,height=40)
#3
def B3_click():
    ent.insert(END,"3")
B3=Button(text="3",font="14",background="#00FFFF",command=B3_click)
B3.place(x=140,y=310,width=40,height=40)
#2
def B2_click():
    ent.insert(END,"2")
B2=Button(text="2",font="14",background="#00FFFF",command=B2_click)
B2.place(x=80,y=310,width=40,height=40)
#1
def B1_click():
    ent.insert(END,"1")
B1=Button(text="1",font="14",background="#00FFFF",command=B1_click)
B1.place(x=20,y=310,width=40,height=40)
#0
def B0_click():
    ent.insert(END,"0")
B0=Button(text="0",font="14",background="#00FFFF",command=B0_click)
B0.place(x=20,y=370,width=100,height=40)
