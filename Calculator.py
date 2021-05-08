from tkinter import*
import math


root =Tk()
root.title("Calculator")
root.geometry("416x550+500+40")

calc =Frame(root, bd=20, pady=5, bg='gainsboro', relief = RIDGE)
calc.grid()

class Calc():
    def __init__(self):
        self.total = 0
        self.current=""
        self.input_value =True
        self.check_sum= False
        self.op=""
        self.result= False

    def insert_value(self, value):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(value)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)


    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, "Wrong Input")

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_Clear_Entry(self):
        self.Clear_Entry()
        self.total=0

    def delectBS(self):
        numLen =len(txtDisplay.get())
        txtDisplay.delete(numLen- 1, 'end')
        if numLen == 1:
            txtDisplay.insert(0, "0")

    def mathsPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(float(txtDisplay.get()))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(float(txtDisplay.get()))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(float(txtDisplay.get()))
        self.display(self.current)


added_value =Calc()

txtDisplay = Entry(calc, font=('arial', 16, 'bold'), bd=20, width=28, justify =RIGHT)
txtDisplay.grid(row =0, column =0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

numberpad ="789456123"
i=0
btn = []
for j in range (3, 6):
    for k in range (3):
        btn.append(Button (calc, activebackground='white', activeforeground='darkslategrey', width=6, height=2, font=('arial', 16, 'bold'), bd=4, text = numberpad[i]))
        btn[i].grid(row=j,column =k, pady=1)
        btn[i]["command"] =lambda x = numberpad[i]: added_value.insert_value(x)
        i += 1
#===============================================================================================================
btnDelete = Button(calc, activebackground='white', width=6, height=2, text="DEL",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.delectBS).grid(row=1, column=0, pady=1)

btnClearAll = Button(calc, activebackground='white', width=6, height=2, text="CE",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.all_Clear_Entry).grid(row=1, column=1, pady=1)
btnClear = Button(calc, activebackground='white', width=6, height=2, text="C",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.Clear_Entry).grid(row=1, column=2, pady=1)
btnPM = Button(calc, activebackground='white', width=6, height=2, text=chr(177),font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.mathsPM).grid(row=1, column=3, pady=1)
#===============================================================================================================
btnSc = Button(calc, activebackground='white', width=6, height=2, text="√",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.squared).grid(row=2, column=0, pady=1)
btnCos = Button(calc, activebackground='white', width=6, height=2, text="Cos",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.cos).grid(row=2, column=1, pady=1)
btnTan = Button(calc, activebackground='white', width=6, height=2, text="Tan",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.tan).grid(row=2, column=2, pady=1)
btnSin = Button(calc, activebackground='white', width=6, height=2, text="Sin",font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=added_value.sin).grid(row=2, column=3, pady=1)

#===============================================================================================================
btnAdd = Button(calc, activebackground='white', width=6, height=2, text="+", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("add")).grid(row=3, column=3, pady=1)
btnSub = Button(calc, activebackground='white', width=6, height=2, text="-", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("sub")).grid(row=4, column=3, pady=1)
btnMulti = Button(calc, activebackground='white', width=6, height=2, text="×", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("multi")).grid(row=5, column=3, pady=1)
btnDiv = Button(calc, activebackground='white', width=6, height=2, text="÷", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command=lambda: added_value.operation("divide")).grid(row=6, column=3, pady=1)
#===============================================================================================================
btnZero = Button(calc, activebackground='white', width=6, height=2, text="0", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command = lambda: added_value.insert_value('0')).grid(row=6, column=0, pady=1)
btnDot = Button(calc, activebackground='white', width=6, height=2, text=".", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command = lambda: added_value.insert_value('.')).grid(row=6, column=1, pady=1)
btnEquals = Button(calc, activebackground='white', width=6, height=2, text="=", font=('arial', 16, 'bold'),bd=4, bg="gainsboro",
                   command = added_value.sum_of_total).grid(row=6, column=2, pady=1)

root.mainloop()
