import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

calculation=""
def addtocalculation(symbol):
    global calculation
    calculation+=str(symbol)
    textresult.delete(1.0,"end")
    textresult.insert(1.0,calculation)
def evaluatecalculation():
    global  calculation
    try:
        result=str(eval(calculation))
        calculation=""
        textresult.delete(1.0,"end")
        textresult.insert(1.0,result)
    except:
        clearfield()
        textresult.insert(1.0,"error")
def clearfield():
    global  calculation
    calculation=""
    textresult.delete(1.0,'end')

root=tk.Tk()
root.geometry("400x300")
root.title("Calculator App")




textresult=tk.Text(root,height=2,width=22,font=("arial",24))
textresult.grid(columnspan=5)
btn1 = tk.Button(root, text="1", command=lambda: addtocalculation(1), width=5, font=("arial", 14))
btn1.grid(row=2, column=1)

btn2 = tk.Button(root, text="2", command=lambda: addtocalculation(2), width=5, font=("arial", 14))
btn2.grid(row=2, column=2)

btn3 = tk.Button(root, text="3", command=lambda: addtocalculation(3), width=5, font=("arial", 14))
btn3.grid(row=2, column=3)

btn4 = tk.Button(root, text="4", command=lambda: addtocalculation(4), width=5, font=("arial", 14))
btn4.grid(row=3, column=1)

btn5 = tk.Button(root, text="5", command=lambda: addtocalculation(5), width=5, font=("arial", 14))
btn5.grid(row=3, column=2)

btn6 = tk.Button(root, text="6", command=lambda: addtocalculation(6), width=5, font=("arial", 14))
btn6.grid(row=3, column=3)

btn7 = tk.Button(root, text="7", command=lambda: addtocalculation(7), width=5, font=("arial", 14))
btn7.grid(row=4, column=1)

btn8 = tk.Button(root, text="8", command=lambda: addtocalculation(8), width=5, font=("arial", 14))
btn8.grid(row=4, column=2)

btn9 = tk.Button(root, text="9", command=lambda: addtocalculation(9), width=5, font=("arial", 14))
btn9.grid(row=4, column=3)

btn0 = tk.Button(root, text="0", command=lambda: addtocalculation(0), width=5, font=("arial", 14))
btn0.grid(row=5, column=2)

btnplus = tk.Button(root, text="+", command=lambda: addtocalculation("+"), width=5, font=("arial", 14))
btnplus.grid(row=2, column=4)

btnminus = tk.Button(root, text="-", command=lambda: addtocalculation("-"), width=5, font=("arial", 14))
btnminus.grid(row=3, column=4)

btnmultiply = tk.Button(root, text="*", command=lambda: addtocalculation("*"), width=5, font=("arial", 14))
btnmultiply.grid(row=4, column=4)

btndivide = tk.Button(root, text="/", command=lambda: addtocalculation("/"), width=5, font=("arial", 14))
btndivide.grid(row=5, column=4)

btnopen = tk.Button(root, text="(", command=lambda: addtocalculation("("), width=5, font=("arial", 14))
btnopen.grid(row=5, column=1)

btnclose = tk.Button(root, text=")", command=lambda: addtocalculation(")"), width=5, font=("arial", 14))
btnclose.grid(row=5, column=3)

btnequal = tk.Button(root, text="=", command=evaluatecalculation, width=14, font=("arial", 14))
btnequal.grid(row=6, column=3,columnspan=2)

btnclear = tk.Button(root, text="C", command=clearfield, width=13, font=("arial", 14))
btnclear.grid(row=6, column=1,columnspan=2)

root.mainloop()
