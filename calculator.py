from tkinter import *
window=Tk()
window.geometry("335x300")
window.resizable(0,0)
window.title("Calculator by Akash")
window.configure(background="black")

def backspace(e):
    '''delete the on char from right'''
    if ans.get() == "invalid":
        ans.set("")
    else:
        ans.set(ans.get()[:len(ans.get()) - 1])

def cal(b):
    '''manage the clear and equal button'''
    if b=="AC":
        ans.set("")
    elif b=="back":
        backspace(b)
    elif b=="equal":
        try:
            if "." in str(eval(ans.get())):
                ans.set("%.3f"%eval(ans.get()))
            else:
                ans.set(eval(ans.get()))
        except:
            ans.set("invalid")
    pass


ans=StringVar()

#display
display=Label(window,text=6,textvariable=ans,height=2,width=22,font=("Arial",20),fg="black",bg="gray")
display.grid(row=0,column=0,pady=1,rowspan=2,columnspan=4,sticky=W)

# first line
openbra=Button(window,text="(",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"("))
openbra.grid(row=2,column=0)
window.bind("<KeyRelease-parenleft>",lambda e :ans.set(ans.get()+"("))

closebra=Button(window,text=")",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+")"))
closebra.grid(row=2,column=1)
window.bind("<KeyRelease-parenright>",lambda e :ans.set(ans.get()+")"))

back=Button(window,text="back",font=("Arial",15),width=5,command=lambda :cal("back"))
back.grid(row=2,column=2)
window.bind("<BackSpace>",backspace)

clean=Button(window,text="AC",font=("Arial",15),width=5,command=lambda :cal("AC"))
clean.grid(row=2,column=3)
window.bind("<Delete>",lambda e:ans.set(""))

# second line
b7=Button(window,text="7",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"7"))
b7.grid(row=3,column=0)
window.bind("7",lambda e :ans.set(ans.get()+"7"))

b8=Button(window,text="8",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"8"))
b8.grid(row=3,column=1)
window.bind("8",lambda e :ans.set(ans.get()+"8"))

b9=Button(window,text="9",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"9"))
b9.grid(row=3,column=2)
window.bind("9",lambda e :ans.set(ans.get()+"9"))

div=Button(window,text="/",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"/"))
div.grid(row=3,column=3)
window.bind("<slash>",lambda e :ans.set(ans.get()+"/"))

# third line
b4=Button(window,text="4",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"4"))
b4.grid(row=4,column=0)
window.bind("4",lambda e :ans.set(ans.get()+"4"))

b5=Button(window,text="5",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"5"))
b5.grid(row=4,column=1)
window.bind("5",lambda e :ans.set(ans.get()+"5"))

b6=Button(window,text="6",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"6"))
b6.grid(row=4,column=2)
window.bind("6",lambda e :ans.set(ans.get()+"6"))

mul=Button(window,text="*",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"*"))
mul.grid(row=4,column=3)
window.bind("<asterisk>",lambda e :ans.set(ans.get()+"*"))

# forth line
b1=Button(window,text="1",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"1"))
b1.grid(row=5,column=0)
window.bind("1",lambda e :ans.set(ans.get()+"1"))

b2=Button(window,text="2",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"2"))
b2.grid(row=5,column=1)
window.bind("2",lambda e :ans.set(ans.get()+"2"))

b3=Button(window,text="3",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"3"))
b3.grid(row=5,column=2)
window.bind("3",lambda e :ans.set(ans.get()+"3"))

Sub=Button(window,text="-",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"-"))
Sub.grid(row=5,column=3)
window.bind("-",lambda e :ans.set(ans.get()+"-"))

# fifth line
b0=Button(window,text="0",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"0"))
b0.grid(row=6,column=0)
window.bind("0",lambda e :ans.set(ans.get()+"0"))

dot=Button(window,text=".",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"."))
dot.grid(row=6,column=1)
window.bind(".",lambda e :ans.set(ans.get()+"."))

equal=Button(window,text="=",font=("Arial",15),width=5,command=lambda :cal("equal"))
equal.grid(row=6,column=2)
window.bind("=",lambda e:cal("equal"))

Add=Button(window,text="+",font=("Arial",15),width=5,command=lambda :ans.set(ans.get()+"+"))
Add.grid(row=6,column=3)
window.bind("+",lambda e :ans.set(ans.get()+"+"))

l=Label(window,text="use keyboard and mouse both\nThank you",fg="purple")
l.grid(row=7,column=0,columnspan=4,pady=6)
window.mainloop()