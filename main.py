from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk()
root.geometry('300x300')
root.title('calculator')
root.resizable(False,False)
root.configure(bg='#212121')
title = Label(root, text="Calculator By M0HA", fg='#d50000',bg='#212121',font=('tajawal',16,'bold'))
title.pack(fill=X)

output = None
def Operator():
    try:
        num1 = int(en1.get())
        Op = cmbol.get()
        num2 = int(en3.get())
        if Op == "+":
            output = num1 + num2
            messagebox.showinfo('Calculator',f'Result : {output}')
        elif Op == "-":
            output = num1 - num2
            messagebox.showinfo('Calculator',f'Result : {output}')
        elif Op == "/":
            output = num1 / num2
            messagebox.showinfo('Calculator',f'Result : {output}')
        elif Op == "*":
            output = num1 * num2
            messagebox.showinfo('Calculator',f'Result : {output}')

    except:
        messagebox.showerror('erorr','Please fill in the fields')
l1 = Label(root, text='Number One :',fg='white',bg='#212121',font=('tajawal',12,'bold'))
l1.place(x=0,y=40)

o1 = Label(root, text='Operator :',fg='white',bg='#212121',font=('tajawal',12,'bold'))
o1.place(x=0,y=80)

l2 = Label(root, text='Number Two :',fg='white',bg='#212121',font=('tajawal',12,'bold'))
l2.place(x=0,y=120)

en1 = Entry(root, font=('tajawal',10))
en1.place(x=120,y=40)
en3 = Entry(root, font=('tajawal',10))
en3.place(x=120,y=120)

cmbol = ttk.Combobox(root, value=('+','/','*','-'),state='readonly')
cmbol.place(x=120,y=80)
result = Button(root,text='result',width=26,fg="#d50000",bg='#212121',font=('tajawal',11,'bold'),command=Operator)
result.place(x=30,y=200)
root.mainloop()