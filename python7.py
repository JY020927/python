from tkinter import *
from tkinter import messagebox

x=Tk()

def b1():
    messagebox.showinfo("top" , "top 버튼 클릭됨")
def b2():
    messagebox.showinfo("bottom" , "bottom 버튼 클릭됨")
def b3():
    messagebox.showinfo("left" , "left 버튼 클릭됨")
def b4():
    messagebox.showinfo("right" , "right 버튼 클릭됨")
def b5():
    messagebox.showinfo("center" , "center 버튼 클릭됨")

b1=Button(x, text="top", width=35, command=b1)
b2=Button(x, text="bottom", width=8, command=b2)
b3=Button(x, text="left", width=3, height=7, command=b3)
b4=Button(x, text="right", width=4, command=b4)
b5=Button(x, text="center", width=10, command=b5)

b1.pack(side=TOP, fill=X)
b2.pack(side=BOTTOM)
b3.pack(side=LEFT, fill=Y)
b4.pack(side=RIGHT)
b5.pack( fill=X, padx=50, pady=50)

x.mainloop()
