from tkinter import *
def press_button(num):

    global equation_txt
    equation_txt=equation_txt+str(num)
    equation_label.set(equation_txt)
def equal():
    global equation_txt
    try:
        total=str(eval(equation_txt))
        equation_label.set(total)
        equation_txt=total
    except ZeroDivisionError:
        equation_label.set("Artmetic Error")
    except SyntaxError:
        equation_label.set("Invalid Synatx")
def clear():
    global equation_txt
    equation_label.set("")
    equation_txt=""
window=Tk()
equation_txt=""
equation_label=StringVar()
window.geometry("500x500")
window.title("Calculator")
label=Label(window,font=("Consolas",20),width=19,height=2,
            bg="black",fg="#00FF00",textvariable=equation_label)
label.pack()
frame=Frame(window,bg="orange")
frame.pack()
button1=Button(frame,text=1,height=4,width=9,command=lambda:press_button(1),bg="#ff7433",fg="#ffffff")
button1.grid(row=0,column=0)

button2=Button(frame,text=2,height=4,width=9,command=lambda:press_button(2),bg="#ff7433",fg="#ffffff")
button2.grid(row=0,column=1)

button3=Button(frame,text=3,height=4,width=9,command=lambda:press_button(3),bg="#ff7433",fg="#ffffff")
button3.grid(row=0,column=2)

button4=Button(frame,text=4,height=4,width=9,command=lambda:press_button(4),bg="#ff7433",fg="#ffffff")
button4.grid(row=1,column=0)

button5=Button(frame,text=5,height=4,width=9,command=lambda:press_button(5),bg="#ff7433",fg="#ffffff")
button5.grid(row=1,column=1)

button6=Button(frame,text=6,height=4,width=9,command=lambda:press_button(6),bg="#ff7433",fg="#ffffff")
button6.grid(row=1,column=2)

button7=Button(frame,text=7,height=4,width=9,command=lambda:press_button(7),bg="#ff7433",fg="#ffffff")
button7.grid(row=2,column=0)

button8=Button(frame,text=8,height=4,width=9,command=lambda:press_button(8),bg="#ff7433",fg="#ffffff")
button8.grid(row=2,column=1)

button9=Button(frame,text=9,height=4,width=9,command=lambda:press_button(9),bg="#ff7433",fg="#ffffff")
button9.grid(row=2,column=2)

button0=Button(frame,text=0,height=4,width=9,command=lambda:press_button(0),bg="#ff7433",fg="#ffffff")
button0.grid(row=3,column=0)

minus=Button(frame,text='-',height=4,width=9,command=lambda:press_button("-"),bg="#ff7433",fg="#ffffff")
minus.grid(row=1,column=3)

mul=Button(frame,text='*',height=4,width=9,command=lambda:press_button("*"),bg="#ff7433",fg="#ffffff")
mul.grid(row=2,column=3)

div=Button(frame,text='/',height=4,width=9,command=lambda:press_button("/"),bg="#ff7433",fg="#ffffff")
div.grid(row=3,column=3)

plus=Button(frame,text='+',height=4,width=9,command=lambda:press_button("+"),bg="#ff7433",fg="#ffffff")
plus.grid(row=0,column=3)
decimal=Button(frame,text='.',height=4,width=9,command=lambda:press_button("."),bg="#ff7433",fg="#ffffff")
decimal.grid(row=3,column=2)
equals=Button(frame,text='=',height=4,width=9,command=equal,bg="#ff7433",fg="#ffffff")
equals.grid(row=3,column=1)
clears=Button(window,text='clear',height=4,width=9,command=clear,bg="#ff7433",fg="#ffffff")
clears.pack()
window.mainloop()