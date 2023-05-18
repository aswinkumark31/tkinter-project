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

x=Button(text='submit',padx=10,pady=5,bg='black',fg='white')
x.pack()
x.place(x=200,y=300)

w.mainloop()