from tkinter import *

w=Tk()
w.geometry('800x800')
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

def display():
    u=Label(text="stud name : "+b.get())
    u.pack()
    u.place(x=50,y=400)
    v=Label(text="enrol no. :"+d.get())
    v.pack()
    v.place(x=50,y=430)
    w=Label(text="GRADE CARD")
    w.pack()
    w.place(x=50,y=480)
    x=Label(text="out of 400")
    x.pack()
    x.place(x=50,y=510)
    y=Label(text="subjects")
    y.pack()
    y.place(x=100,y=540)
    z=Label(text="marks")
    z.pack()
    z.place(x=350,y=540)
    xy=Label(text="grade")
    xy.pack()
    xy.place(x=550,y=540)
    yz=Label(text="english")
    yz.pack()
    yz.place(x=100,y=570)
    xz=Label(text=i.get())
    xz.pack()
    xz.place(x=350,y=570)
    ab=Label(text=j.get())
    ab.pack()
    ab.place(x=550,y=570)
    bc=Label(text="Hindi")
    bc.pack()
    bc.place(x=100,y=600)
    ac=Label(text=n.get())
    ac.pack()
    ac.place(x=350,y=600)
    ad=Label(text=m.get())
    ad.pack()
    ad.place(x=550,y=600)
    ce=Label(text="Science")
    ce.pack()
    ce.place(x=100,y=630)
    cd=Label(text=p.get())
    cd.pack()
    cd.place(x=350,y=630)
    de=Label(text=q.get())
    de.pack()
    de.place(x=550,y=630)
    af=Label(text="Maths")
    af.pack()
    af.place(x=100,y=660)
    fg=Label(text=s.get())
    fg.pack()
    fg.place(x=350,y=660)
    df=Label(text=t.get())
    df.pack()
    df.place(x=550,y=660)

    nk=Label(text="your total score is :")
    nk.pack()
    nk.place(x=50,y=700)  
    az=Label(text= int(i.get())+int(n.get())+int(p.get())+int(s.get()))
    az.pack()
    az.place(x=200,y=700)
    
    yk=Label(text="your percentage is :")
    yk.pack()
    yk.place(x=50,y=730)
    ay=Label(text=(int(i.get())+int(n.get())+int(p.get())+int(s.get()))*100/400)
    ay.pack()
    ay.place(x=200,y=730)



x=Button(text='submit',command=display,padx=10,pady=5,bg='blue',fg='white')
x.pack()
x.place(x=600,y=350)

w.mainloop()




