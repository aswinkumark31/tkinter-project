from tkinter import *

w=Tk()
w.geometry('600x800')
w.resizable(False,False)

a=Label(text='Registration form')
a.config(font=('arial',20))
a.pack()
a.place(x=200,y=30)


b=Label(text='username')
b.pack()
b.place(x=30,y=100)

e=Entry(width=30)
e.pack()
e.place(x=150,y=100)

c=Label(text='Password')
c.pack()
c.place(x=30,y=150)

f=Entry(width=30)
f.pack()
f.place(x=150,y=150)

d=Label(text='DOB')
d.pack()
d.place(x=30,y=200)

g=Entry(width=30)
g.pack()
g.place(x=150,y=200)

def display():
    la = Label(text="welcome "+e.get())
    la.pack()
    la.place(x=180,y=450)
    l=Label(text="your password is "+f.get())
    l.pack()
    l.place(x=180,y=500)
    lab=Label(text="your DOB is "+g.get())
    lab.pack()
    lab.place(x=180,y=550) 


x=Button(text='submit',command=display,padx=10,pady=5,bg='black',fg='white')
x.pack()
x.place(x=200,y=300)

w.mainloop()