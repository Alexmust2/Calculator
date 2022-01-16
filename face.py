import tkinter
from tkinter.constants import COMMAND, END, FIRST, MULTIPLE, X, Y
import re
import math


window = tkinter.Tk()
window.title ("Calculator")
window.geometry("270x405")
data = tkinter.StringVar()
expression = ""
result = ""
entry = tkinter.Entry(window, textvariable=data, width=50)
entry.place(x=0, y=0, height=82)

def nums(number):
    global expression
    expression += str(number)
    data.set (expression)


def arithmetic(expression):
    global result
    operators = "+-*/%"
    operator = ""
    for char in expression:
        if char in operators:
            operator = char
            if len(operators) > 2:
                clear()
    data.set("Error")
    operator_pos = expression.index(operator)
    first_number = expression[0 : operator_pos]
    second_number = expression[operator_pos + 1:]
    if operator == "+":
        result = data.set(int(first_number) + int(second_number))
    elif operator == "-":
        result = data.set(int(first_number) - int(second_number))
    elif operator == "*":
        result = data.set(int(first_number) * int(second_number))
    elif operator == "/":
        result = data.set(int(first_number) / int(second_number))
    elif operator == "%":
        result = data.set(int(first_number) / 100)
    result = data.get()
    expression = result
    data.set (expression)
    if expression == result:
        clear()
    data.set(result)

    
def clear():
    global expression
    expression = ""
    data.set("")

    

open_parenthesis_button = tkinter.Button(window, text="(", height=3, width=5,)
open_parenthesis_button.place(x=0, y=80)

closed_parenthesis_button = tkinter.Button(window, text=")", height=3, width=5,)
closed_parenthesis_button.place(x=67, y=80)

percent_button = tkinter.Button(window, text = "%", height=3, width=5, command=lambda:nums("%"))
percent_button.place(x=134, y=80)

clear_button = tkinter.Button(window, text="AC", height=3, width=5, command=lambda:clear())
clear_button.place(x=201, y=80)

button_1 = tkinter.Button(window, text="1", height=3, width=5, command=lambda:nums(1))
button_1.place(x=0, y=145)

button_2 = tkinter.Button(window,text="2", height=3, width=5, command=lambda:nums(2))
button_2.place(x=67, y=145)

button_3 = tkinter.Button(window,text="3", height=3, width=5, command=lambda:nums(3))
button_3.place(x=134, y=145)

button_4 = tkinter.Button(window,text="4", height=3, width=5, command=lambda:nums(4))
button_4.place(x=0, y=210)

button_5 = tkinter.Button(window,text="5", height=3, width=5, command=lambda:nums(5))
button_5.place(x=67, y=210)

button_6 = tkinter.Button(window,text="6", height=3, width=5, command=lambda:nums(6))
button_6.place(x=134, y=210)

button_7 = tkinter.Button(window,text="7", height=3, width=5, command=lambda:nums(7))
button_7.place(x=0, y=275)

button_8 = tkinter.Button(window,text="8", height=3, width=5, command=lambda:nums(8))
button_8.place(x=67, y=275)

button_9 = tkinter.Button(window,text="9", height=3, width=5, command=lambda:nums(9))
button_9.place(x=134, y=275)

button_0 = tkinter.Button(window,text="0", height=3, width=5, command=lambda:nums(0))
button_0.place(x=0, y=340)

decimal_button = tkinter.Button(window,text=".", height=3, width=5, command=lambda:nums("."))
decimal_button.place(x=67, y=340)

division_button = tkinter.Button(window,text="/", height=3, width=5, command=lambda:nums("/"))
division_button.place(x=201, y=145)

multiplication_button = tkinter.Button(window, text="*", height=3, width=5, command=lambda:nums("*"))
multiplication_button.place(x=201, y=210)

minus_button = tkinter.Button(window, text="-", height=3, width=5, command=lambda:nums("-"))
minus_button.place(x=201, y=275)

equals_button = tkinter.Button(window, text="=", height=3, width=5, command=lambda:arithmetic(expression))
equals_button.place(x=134, y=340)

summ_button = tkinter.Button(window, text="+", height=3, width=5, command=lambda:nums("+"))
summ_button.place(x=201, y=340)


window.mainloop()