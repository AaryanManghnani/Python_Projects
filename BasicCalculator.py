from tkinter import *
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

root = Tk()
root.title("Calculator")

e = Entry(root,width =40,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=5)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_back():
    e.delete(len(e.get())-1)

X = ""
Y = 0 

def get_value():
    num = e.get()
    try:
        return int(num)
    except ValueError:
        return None

def button_fun(operation):
    global X 
    global Y
    X = operation
    Y = get_value()
    e.delete(0,END)

def button_equals():
    total = ops[X](Y,get_value())
    e.delete(0,END)
    e.insert(0,total)

button0 = Button(root,text = "0",padx =92.5,pady=15,command=lambda: button_click(0))
button1 = Button(root,text = "1",padx =25,pady=15,command=lambda: button_click(1))
button2 = Button(root,text = "2",padx =25,pady=15,command=lambda: button_click(2))
button3 = Button(root,text = "3",padx =25,pady=15,command=lambda: button_click(3))
button4 = Button(root,text = "4",padx =25,pady=15,command=lambda: button_click(4))
button5 = Button(root,text = "5",padx =25,pady=15,command=lambda: button_click(5))
button6 = Button(root,text = "6",padx =25,pady=15,command=lambda: button_click(6))
button7 = Button(root,text = "7",padx =25,pady=15,command=lambda: button_click(7))
button8 = Button(root,text = "8",padx =25,pady=15,command=lambda: button_click(8))
button9 = Button(root,text = "9",padx =25,pady=15,command=lambda: button_click(9))

buttonAdd = Button(root,text = "+",padx =23.5,pady=15,command=lambda: button_fun('+'))
buttonSub = Button(root,text = "-",padx =25,pady=15,command=lambda: button_fun('-'))
buttonMul = Button(root,text = "x",padx =25,pady=15,command=lambda: button_fun('*'))
buttonDiv = Button(root,text = "/",padx =25,pady=15,command=lambda: button_fun('/'))
buttonEq = Button(root,text = "=",padx =23.5,pady=15,command=button_equals)
buttonCE = Button(root,text = "CE",padx =55,pady=15,command=button_clear)
buttonBS = Button(root,text = "Back",padx =15,pady=15,command=button_back)


button1.grid(column=0 ,row=4)
button2.grid(column=1 ,row=4)
button3.grid(column=2 ,row=4)
button4.grid(column=0 ,row=3)
button5.grid(column=1 ,row=3)
button6.grid(column=2 ,row=3)
button7.grid(column=0 ,row=2)
button8.grid(column=1 ,row=2)
button9.grid(column=2 ,row=2)
button0.grid(column=0,row=5,columnspan=3)

buttonAdd.grid(column=3,row=5)
buttonSub.grid(column=3,row=4)
buttonMul.grid(column=3,row=3)
buttonDiv.grid(column=3,row=2)
buttonEq.grid(column=3,row=1)
buttonCE.grid(column=0,row=1,columnspan=2)
buttonBS.grid(column=2,row=1)

root.mainloop()