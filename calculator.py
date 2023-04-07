from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def buttonClick(number):
    current = e.get()
    output = current + str(number)
    e.delete(0,END)
    e.insert(0,output)

def allClear():
    e.delete(0,END)

def swapSign():
    current = e.get()
    currentNum = float(current)
    if currentNum == int(currentNum):
        currentNum = int(currentNum)
    currentNum *= -1
    e.delete(0,END)
    e.insert(0,str(currentNum))

def remainder():
    firstNumber = e.get() 
    global numFirstForRemainder
    global operator
    operator = "remainder"
    numFirstForRemainder = float(firstNumber)
    if numFirstForRemainder == int(numFirstForRemainder):
        numFirstForRemainder = int(numFirstForRemainder)
    e.delete(0,END)

def equal():
    secondNumber = e.get()
    res = 0
    if operator == "add":
        newSecond = float(secondNumber)
        if newSecond == int(newSecond):
            newSecond = int(newSecond)
        res = numFirstForAdd + newSecond
        if res == int(res):
            res = int(res)

    elif operator == "subtract":
        newSecond = float(secondNumber)
        if newSecond == int(newSecond):
            newSecond = int(newSecond)
        res = numFirstForSubtract - newSecond
        if res == int(res):
            res = int(res)

    elif operator == "multiply":
        newSecond = float(secondNumber)
        if newSecond == int(newSecond):
            newSecond = int(newSecond)
        res = numFirstForMultiply * newSecond
        if res == int(res):
            res = int(res)

    elif operator == "divide":
        newSecond = float(secondNumber)
        if newSecond == int(newSecond):
            newSecond = int(newSecond)
        res = numFirstForDivide / newSecond
        if int(res) == res:
            res = int(res)
    else:
        newSecond = float(secondNumber)
        if newSecond == int(newSecond):
            newSecond = int(newSecond)
        if type(newSecond) != int or type(numFirstForRemainder) != int:
            e.delete(0,END)
            e.insert(0,"ERROR")
            return
        res = numFirstForRemainder % newSecond
        if int(res) == res:
            res = int(res)
    e.delete(0,END)
    e.insert(0,str(res))

def add():
    firstNumber = e.get()
    global numFirstForAdd
    global operator
    operator = "add"
    numFirstForAdd = float(firstNumber)
    if numFirstForAdd == int(numFirstForAdd):
        numFirstForAdd = int(numFirstForAdd)
    e.delete(0,END)

def subtract():
    firstNumber = e.get()
    global numFirstForSubtract
    global operator
    operator = "subtract"
    numFirstForSubtract = float(firstNumber)
    if numFirstForSubtract == int(numFirstForSubtract):
        numFirstForSubtract = int(numFirstForSubtract)
    e.delete(0,END)

def multiply():
    firstNumber = e.get()
    global numFirstForMultiply
    global operator
    operator = "multiply"
    numFirstForMultiply = float(firstNumber)
    if numFirstForMultiply == int(numFirstForMultiply):
        numFirstForMultiply = int(numFirstForMultiply)
    e.delete(0,END)

def divide():
    firstNumber = e.get()
    global numFirstForDivide
    global operator
    operator = "divide"
    numFirstForDivide = float(firstNumber)
    if numFirstForDivide == int(numFirstForDivide):
        numFirstForDivide = int(numFirstForDivide)
    e.delete(0,END)

def dot():
    current = e.get()
    e.delete(0,END)
    global dotCnt
    currentNum = float(current)
    if int(currentNum) == currentNum:
        dotCnt = 0
    else:
        dotCnt = 1

    if dotCnt == 0:
        e.insert(0,current+'.')
    else:
        e.insert(0, "ERROR")

#Create Button Objects
button1 = Button(root, text="1", padx=40, pady=40, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=40, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=40, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=40, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=40, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=40, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=40, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=40, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=40, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=100, pady=40, command=lambda: buttonClick(0))
buttonAC = Button(root, text="AC", padx=35, pady=40, command=allClear)
buttonSwapSign = Button(root, text="+/-",padx=35, pady=40,command=swapSign)
buttonRemainder = Button(root, text="%", padx=40, pady=40, command=remainder)
buttonEquals = Button(root, text="=",padx=40, pady=40,command=equal)
buttonAdd = Button(root, text="+", padx=40, pady=40, command=add)
buttonSubtraction = Button(root, text="-", padx=40, pady=40, command=subtract)
buttonMultiplication = Button(root, text="*", padx=40, pady=40, command=multiply)
buttonDivision = Button(root, text="/", padx=40, pady=40, command=divide)
buttonDot = Button(root, text=".", padx=43, pady=40, command=dot)


#Decide location of each Button
buttonAC.grid(row=1,column=0)
buttonSwapSign.grid(row=1,column=1)
buttonRemainder.grid(row=1,column=2)
buttonDivision.grid(row=1,column=3)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonMultiplication.grid(row=2,column=3)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonSubtraction.grid(row=3,column=3)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
buttonAdd.grid(row=4,column=3)
button0.grid(row=5,column=0, columnspan=2)
buttonDot.grid(row=5,column=2)
buttonEquals.grid(row=5,column=3)
root.mainloop()
