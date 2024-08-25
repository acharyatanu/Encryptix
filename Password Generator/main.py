from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_char=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_char
    password_len=int(length_box.get())

    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_len))

    if choice.get()==2:
        passwordfield.insert(1,random.sample(small_alphabets+capital_alphabets,password_len))

    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_len))
    #password=random.sample(all,password_len)
    #passwordfield.insert(0,password)


def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)


root=Tk()

root.config(bg="gray20")
choice=IntVar()
Font=('arial', 13,'bold')


label=Label(root,text="Password Generator",font=('times new roman' ,20 ,'bold'),bg="gray20",fg="white")
label.grid(pady=10)

weakbutton=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font)
weakbutton.grid(pady=5)

mediumbutton=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font)
mediumbutton.grid(pady=5)

strongbutton=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font)
strongbutton.grid(pady=5)

lengthlabel=Label(root,text="Password Length",font=Font,bg="gray20",fg="white")
lengthlabel.grid()

length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.grid()

generatebutton=Button(root,text="Generate",font=Font,command=generator)
generatebutton.grid(pady=5)

passwordfield=Entry(root,width=25,bd=2,font=Font)
passwordfield.grid()

copybutton=Button(root,text="Copy",font=Font,command=copy)
copybutton.grid(pady=5)



root.mainloop()