import tkinter as tk
equation = []
number1 = 0
number2 = 0
finalequation = ""
operation = ""
def insert0():
    global equation
    equation.append(0)
    text.insert(tk.END, 0)
def insert1():
    global equation
    equation.append(1)
    text.insert(tk.END, 1)
def insert2():
    global equation
    equation.append(2)
    text.insert(tk.END, 2)
def insert3():
    global equation
    equation.append(3)
    text.insert(tk.END, 3)
def insert4():
    global equation
    equation.append(4)
    text.insert(tk.END, 4)
def insert5():
    global equation
    equation.append(5)
    text.insert(tk.END, 5)
def insert6():
    global equation
    equation.append(6)
    text.insert(tk.END, 6)
def insert7():
    global equation
    equation.append(7)
    text.insert(tk.END, 7)
def insert8():
    global equation
    equation.append(8)
    text.insert(tk.END, 8)
def insert9():
    global equation
    equation.append(9)
    text.insert(tk.END, 9)
def add():
    global equation
    global number1
    global operation
    number1 = ''.join(map(str, equation))
    number1 = int(number1)
    operation="+"
    equation=[]
    text.insert(tk.END, "+")
def subtract():
    global equation
    global number1
    global operation
    number1 = ''.join(map(str, equation))
    number1 = int(number1)
    operation="-"
    equation=[]
    text.insert(tk.END, "-")
def multiply():
    global equation
    global number1
    global operation
    number1 = ''.join(map(str, equation))
    number1 = int(number1)
    operation="*"
    equation=[]
    text.insert(tk.END, "*")
def divide():
    global equation
    global number1
    global operation
    number1 = ''.join(map(str, equation))
    number1 = int(number1)
    operation="/"
    equation=[]
    text.insert(tk.END, "/")
def solve():
    global equation
    global number1
    global number2
    global finalequation
    global operation
    number2 = ''.join(map(str, equation))
    number2 = int(number2)
    finalequation=int(eval(str(number1)+str(operation)+str(number2)))
    text.insert(tk.END, "=")
    text.insert(tk.END, finalequation)
def clear():
    global equation
    global number1
    global number2
    global finalequation
    global operation
    equation=[]
    operation=""
    number1=0
    number2=0
    text.delete("1.0", tk.END)
def ans():
    global finalequation
    global equation
    equation.append(finalequation)
    text.insert(tk.END, finalequation)
root=tk.Tk()
root.title("Calculator")
text=tk.Text(root, width=15, height=1)
text.grid(row=0, column=0, columnspan=4)
button1 = tk.Button(root, text="1", command=insert1, padx=0, pady=0)
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="2", command=insert2, padx=0, pady=0)
button2.grid(row=1, column=1)
button3 = tk.Button(root, text="3", command=insert3, padx=0, pady=0)
button3.grid(row=1, column=2)
button4 = tk.Button(root, text="4", command=insert4, padx=0, pady=0)
button4.grid(row=2, column=0)
button5 = tk.Button(root, text="5", command=insert5, padx=0, pady=0)
button5.grid(row=2, column=1)
button6 = tk.Button(root, text="6", command=insert6, padx=0, pady=0)
button6.grid(row=2, column=2)
button7 = tk.Button(root, text="7", command=insert7, padx=0, pady=0)
button7.grid(row=3, column=0)
button8 = tk.Button(root, text="8", command=insert8, padx=0, pady=0)
button8.grid(row=3, column=1)
button9 = tk.Button(root, text="9", command=insert9, padx=0, pady=0)
button9.grid(row=3, column=2)
button0 = tk.Button(root, text="0", command=insert0, padx=0, pady=0)
button0.grid(row=4, column=1)
buttonadd=tk.Button(root, text="+", command=add, padx=0, pady=0)
buttonadd.grid(row=1, column=3)
buttonsubtract=tk.Button(root, text="-", command=subtract)
buttonsubtract.grid(row=2, column=3)
buttonmultiply=tk.Button(root, text="×", command=multiply, padx=0, pady=0)
buttonmultiply.grid(row=3, column=3)
buttondivide=tk.Button(root, text="÷", command=divide, padx=0, pady=0)
buttondivide.grid(row=4, column=3)
buttonans=tk.Button(root, text="=", command=solve, padx=0, pady=0)
buttonans.grid(row=5, column=3)
buttonclear=tk.Button(root, text="CLEAR", command=clear, padx=0, pady=0)
buttonclear.grid(row=5, column=1, rowspan=2)
buttonans=tk.Button(root, text="ANS", command=ans, padx=0, pady=0)
buttonans.grid(row=5, column=0)
root.mainloop()
