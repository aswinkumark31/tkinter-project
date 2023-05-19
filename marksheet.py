from tkinter import *

w=Tk()
w.geometry('800x400')
w.resizable(False,False)

l=Label(text="STUDENT MARK SHEET")
l.config(font=('arial',20))
l.pack()
l.place(x=50,y=20)

a=Label(text="NAME")
a.pack()
a.place(x=50,y=80)

b=Entry(width=20)
b.pack()
b.place(x=100,y=80)

c=Label(text="Enrol no:")
c.pack()
c.place(x=250,y=80)

d=Entry(width=20)
d.pack()
d.place(x=320,y=80)

e=Label(text="SUBJECTS")
e.pack()
e.place(x=100,y=150)

f=Label(text="MARKS")
f.pack()
f.place(x=350,y=150)

g=Label(text="Grade")
g.pack()
g.place(x=550,y=150)

h=Label(text="ENGLISH")
h.pack()
h.place(x=100,y=200)

i=Entry(width=20)
i.pack()
i.place(x=300,y=200)

j=Entry(width=20)
j.pack()
j.place(x=500,y=200)

k=Label(text="HINDI")
k.pack()
k.place(x=100,y=230)

n=Entry(width=20)
n.pack()
n.place(x=300,y=230)

m=Entry(width=20)
m.pack()
m.place(x=500,y=230)

o=Label(text='Science')
o.pack()
o.place(x=100,y=260)

p=Entry(width=20)
p.pack()
p.place(x=300,y=260)

q=Entry(width=20)
q.pack()
q.place(x=500,y=260)

r=Label(text='MATHS')
r.pack()
r.place(x=100,y=290)

s=Entry(width=20)
s.pack()
s.place(x=300,y=290)

t=Entry(width=20)
t.pack()
t.place(x=500,y=290)

x=Button(text='submit',padx=10,pady=5,bg='blue',fg='white')
x.pack()
x.place(x=600,y=350)

w.mainloop()