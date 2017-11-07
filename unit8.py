# By: Magnus Crooke, File Name: unit8.py, Last modified: 11-7-2017, This Program is a calculator.
import tkinter

root = tkinter.Tk()
root.title("Calculator")

answer = tkinter.StringVar()


def press0():
    """
    This function saves the number you click and saves it on the calculator
    """
    zero = answer.get()
    zero = zero + "0"
    answer.set(zero)


def press1():
    """
    This function saves the number you click and saves it on the calculator
    """
    first = answer.get()
    first = first + "1"
    answer.set(first)


def press2():
    """
    This function saves the number you click and saves it on the calculator
    """
    second = answer.get()
    second = second + "2"
    answer.set(second)


def press3():
    """
    This function saves the number you click and saves it on the calculator
    """
    third = answer.get()
    third = third + "3"
    answer.set(third)


def press4():
    """
    This function saves the number you click and saves it on the calculator
    """
    fourth = answer.get()
    fourth = fourth + "4"
    answer.set(fourth)


def press5():
    """
    This function saves the number you click and saves it on the calculator
    """
    fifth = answer.get()
    fifth = fifth + "5"
    answer.set(fifth)


def press6():
    """
    This function saves the number you click and saves it on the calculator
    """
    sixth = answer.get()
    sixth = sixth + "6"
    answer.set(sixth)


def press7():
    """
    This function saves the number you click and saves it on the calculator
    """
    seventh = answer.get()
    seventh = seventh + "7"
    answer.set(seventh)


def press8():
    """
    This function saves the number you click and saves it on the calculator
    """
    eigth = answer.get()
    eigth = eigth + "8"
    answer.set(eigth)


def press9():
    """
    This function saves the number you click and saves it on the calculator
    """
    nineth = answer.get()
    nineth = nineth + "9"
    answer.set(nineth)


def decimal():
    """
    This function saves the decimal point for the answer
    """
    deci = answer.get()
    deci = deci + "."
    answer.set(deci)


def clear():
    """
    This function clears the calculator
    :return:
    """
    answer.set("")


def multiplication():
    """
    This function multiplies the numbers inputted into the calculator
    """
    multi = answer.get()
    multi = multi + "*"
    answer.set(multi)


def division():
    """
    This function divides the numbers inputted into the calculator
    """
    divi = answer.get()
    divi = divi + "/"
    answer.set(divi)


def subtraction():
    """
    This function subtracts the numbers inputted into the calculator
    """
    sub = answer.get()
    sub = sub + "-"
    answer.set(sub)


def addition():
    """
    This function adds the numbers inputted into the calculator
    """
    add = answer.get()
    add = add + "+"
    answer.set(add)


def equals():
    """
    This function outputs the answer to the equation inputted by the user
    """
    eql = answer.get()
    core = eval(eql)
    answer.set(core)


def squared():
    """
    This function squares the input number in the calculator
    """
    x2 = answer.get()
    x2 = float(x2)
    sans = x2 ** 2
    answer.set(str(sans))

Number0Label = tkinter.Button(root, text="0", command=press0)
Number0Label.grid(row=4, column=2)

DecimalLabel = tkinter.Button(root, text=".", command=decimal)
DecimalLabel.grid(row=4, column=3)

ClearLabel = tkinter.Button(root, text="C", command=clear)
ClearLabel.grid(row=4, column=4)

DivisionLabel = tkinter.Button(root, text="/", command=division)
DivisionLabel.grid(row=4, column=5)

Number1Label = tkinter.Button(root, text="1", command=press1)
Number1Label.grid(row=3, column=2)

Number2Label = tkinter.Button(root, text="2", command=press2)
Number2Label.grid(row=3, column=3)

Number3Label = tkinter.Button(root, text="3", command=press3)
Number3Label.grid(row=3, column=4)

SubLabel = tkinter.Button(root, text="-", command=subtraction)
SubLabel.grid(row=3, column=5)

Number4Label = tkinter.Button(root, text="4", command=press4)
Number4Label.grid(row=2, column=2)

Number5Label = tkinter.Button(root, text="5", command=press5)
Number5Label.grid(row=2, column=3)

Number6Label = tkinter.Button(root, text="6", command=press6)
Number6Label.grid(row=2, column=4)

AdditionLabel = tkinter.Button(root, text="+", command=addition)
AdditionLabel.grid(row=2, column=5)

Number7Label = tkinter.Button(root, text="7", command=press7)
Number7Label.grid(row=1, column=2)

Number8Label = tkinter.Button(root, text="8", command=press8)
Number8Label.grid(row=1, column=3)

Number9Label = tkinter.Button(root, text="9", command=press9)
Number9Label.grid(row=1, column=4)

MultiLabel = tkinter.Button(root, text="*", command=multiplication)
MultiLabel.grid(row=1, column=5)

XSquaredLabel = tkinter.Button(root, text="x²", command=squared)
XSquaredLabel.grid(row=1, column=6)

EqualsLabel = tkinter.Button(root, text="=", command=equals)
EqualsLabel.grid(row=2, rowspan=3, column=6, sticky="NS")
root.bind("<Return>", lambda e: equals())

TotalLabel = tkinter.Entry(root, textvariable=answer)
TotalLabel.grid(row=0, columnspan=5, column=2, sticky="EW")

root.mainloop()
