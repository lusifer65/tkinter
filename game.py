from tkinter import *

window=Tk()
window.geometry("500x500")   #size of the window
window.resizable(0,0)
c=1

def clear():       #to clear the text field of the game
    b1["text"]=""
    b2["text"]=""
    b3["text"]=""
    b4["text"]=""
    b5["text"]=""
    b6["text"]=""
    b7["text"]=""
    b8["text"]=""
    b9["text"]=""
    b1["bg"]="white"
    b2["bg"]="white"
    b3["bg"]="white"
    b4["bg"]="white"
    b5["bg"]="white"
    b6["bg"]="white"
    b7["bg"]="white"
    b8["bg"]="white"
    b9["bg"]="white"
    c=1
    l["text"]="well played"
def function(b):
    global c
    message=""

    if b['text']=="":
        c += 1
        if c%2==0:
            b["text"]="O"
            b['bg']="black"
            b['fg']="white"
        else:
            b["text"]="X"
            b['bg']="black"
            b['fg']="white"
    if(b1["text"]=='O' and b2["text"]=='O' and b3["text"]=='O'):
        message="player1 is winner"
    elif b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X':
        message="player2 is winner"
    elif(b4["text"]=='O' and b5["text"]=='O' and b6["text"]=='O'):
        message="player1 is winner"
    elif b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X':
        message="player2 is winner"
    elif(b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O'):
        message="player1 is winner"
    elif b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X':
        message="player2 is winner"
    elif(b1["text"]=='O' and b4["text"]=='O' and b7["text"]=='O'):
        message="player1 is winner"
    elif b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X':
        message="player2 is winner"
    elif(b2["text"]=='O' and b5["text"]=='O' and b8["text"]=='O'):
        message="player1 is winner"
    elif b2["text"]=='X' and b5["text"]=='X' and b8["text"]=='X':
        message="player2 is winner"
    elif(b3["text"]=='O' and b6["text"]=='O' and b9["text"]=='O'):
        message="player1 is winner"
    elif b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X':
        message="player2 is winner"
    elif (b1["text"] == 'O' and b5["text"] == 'O' and b9["text"] == 'O'):
        message = "player1 is winner"
    elif b1["text"] == 'X' and b5["text"] == 'X' and b9["text"] == 'X':
        message = "player2 is winner"
    elif (b3["text"] == 'O' and b5["text"] == 'O' and b7["text"] == 'O'):
        message = "player1 is winner"
    elif b3["text"] == 'X' and b5["text"] == 'X' and b7["text"] == 'X':
        message = "player2 is winner"
    if message!="":
        global l
        l=Label(window,text=message)
        l.grid(row=3,column=0)
        message=""
        b=Button(window,text="play again",command=clear)
        b.grid(row=3,column=1)
    if message=="" and c>9:
        l = Label(window, text=message)
        c=1
        l.grid(row=3, column=0)
        clear()


#driver code
window.title("tic tac toe by Akash")
b1=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b1))
b1.grid(row=0,column=0)
b2=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b2))
b2.grid(row=0,column=1)
b3=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b3))
b3.grid(row=0,column=2)

b4=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b4))
b4.grid(row=1,column=0)
b5=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b5))
b5.grid(row=1,column=1)
b6=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b6))
b6.grid(row=1,column=2)

b7=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b7))
b7.grid(row=2,column=0)
b8=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b8))
b8.grid(row=2,column=1)
b9=Button(window,text="",font=("",15),height=5,width=10,command=lambda :function(b9))
b9.grid(row=2,column=2)

window.mainloop()