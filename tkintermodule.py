from tkinter import *


w=Tk()
w.geometry('600x800')
w.resizable(False,False)
w.title("sample tkinter")
w.configure(background="white")

l=Label(text="username",bg="black",fg="white",width=20,pady=10)
l.pack()
l.place(x=50,y=150)

e=Entry(width=30)
e.pack()
e.place(x=250,y=150)

b = Button(text="click here",padx=10,pady=10)
b.pack()
b.place(x=250,y=700)

w.mainloop()