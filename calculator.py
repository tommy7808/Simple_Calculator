#Created by Ayotomiwa Adekunle

from tkinter import *
from math import sqrt

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.resizable(False, False)

        #state checkers
        self.clicked = False
        self.but_press = False
        self.plus = False
        self.minus1 = False
        self.multiply1 = False
        self.divide1 = False

        #numbers for each operation
        self.addition = 0
        self.minus = 0
        self.multiply = 0
        self.divide = 0

        def button_click(self, number):
            current = self.entry.get()
            self.entry.delete(0, END)
            self.entry.insert(0, str(current) + str(number))

            #Checks if a number is pressed during an operation
            if self.but_press == True:
                self.entry.delete(0, END)
                self.entry.insert(0, str(number))
                self.but_press = False

            
        def clear(self):
            self.entry.delete(0, END)
            #reset values
            self.addition = 0
            self.minus = 0
            self.multiply = 0
            self.divide = 0

        def back(self):
            current = self.entry.get()
            display = current[0:-1]
            self.entry.delete(0, END)
            self.entry.insert(0, display)

        def add(self):
            try:
                number = self.entry.get()
                
                #checks if function has been called already
                if self.addition == 0:
                    self.addition = self.addition + int(number)
                    self.entry.delete(0, END)
                    self.plus = True
                else:
                #if function has already been called before it will add to the addition variable and display its total.
                    self.entry.delete(0, END)
                    self.addition = self.addition + int(number)
                    self.entry.insert(0, self.addition)
                    self.but_press = True
            except ValueError:
                number = self.entry.get()
                
                if self.addition == 0:
                    self.addition = self.addition + float(number)
                    self.entry.delete(0, END)
                    self.plus = True
                else:
                    self.entry.delete(0, END)
                    self.addition = self.addition + float(number)
                    self.entry.insert(0, self.addition)
                    self.but_press = True

        def minus(self):
            try:
                number = self.entry.get()
                
                #checks if function has been called already
                if self.minus == 0:
                    self.minus = self.addition + int(number)
                    self.entry.delete(0, END)
                    self.minus1 = True
                else:
                #if function has already been called before it will perform minus operation
                    self.entry.delete(0, END)
                    self.minus = self.minus - int(number)
                    self.entry.insert(0, self.minus)
                    self.but_press = True

            except ValueError:
                number = self.entry.get()
                
                if self.minus == 0:
                    self.minus = self.addition + float(number)
                    self.entry.delete(0, END)
                    self.minus1 = True
                else:
                    self.entry.delete(0, END)
                    self.minus = self.minus - float(number)
                    self.entry.insert(0, self.minus)
                    self.but_press = True


        def multiply(self):
            try:
                number2 = self.entry.get()

                if self.multiply == 0:
                    self.multiply = self.multiply + int(number2)
                    self.entry.delete(0, END)
                    self.multiply1 = True
                else:
                #if function has already been called before it will perform the multiplication operation.
                    self.entry.delete(0, END)
                    self.multiply = self.multiply * int(number2)
                    self.entry.insert(0, self.multiply)
                    self.but_press = True
            except ValueError:
                number2 = self.entry.get()

                if self.multiply == 0:
                    self.multiply = self.multiply + float(number2)
                    self.entry.delete(0, END)
                    self.multiply1 = True
                else:
                    self.entry.delete(0, END)
                    self.multiply = self.multiply * float(number2)
                    self.entry.insert(0, self.multiply)
                    self.but_press = True


        def square(self):
            try:
                number2 = self.entry.get()
                self.entry.delete(0, END)
                self.entry.insert(0, int(number2) ** 2)

            except ValueError:
                self.entry.delete(0, END)
                self.entry.insert(0, float(number2) ** 2)

        def square_root(self):
            try:
                number2 = self.entry.get()
                self.entry.delete(0, END)
                self.entry.insert(0, sqrt(int(number2)))

            except ValueError:
                self.entry.delete(0, END)
                self.entry.insert(0, sqrt(float(number2)))

        def divide(self):
            try:
                number2 = self.entry.get()

                if self.divide == 0:
                    self.divide = self.divide + int(number2)
                    self.entry.delete(0, END)
                    self.divide1 = True
                else:
                #if function has already been called before it will perform division.
                    self.entry.delete(0, END)
                    self.divide = self.divide / int(number2)
                    self.entry.insert(0, self.divide)
                    self.but_press = True
            except ValueError:
                number2 = self.entry.get()

                if self.divide == 0:
                    self.divide = self.divide + float(number2)
                    self.entry.delete(0, END)
                    self.divide1 = True
                else:
                    self.entry.delete(0, END)
                    self.divide = self.divide / float(number2)
                    self.entry.insert(0, self.divide)
                    self.but_press = True
        
        #This function checks if an operation has been called before it and then for that following operation display the answer.
        def equal(self):
            if self.plus:
                try:
                    number1 = self.entry.get()
                    self.entry.delete(0, END)
                    self.addition = self.addition + int(number1)
                    self.entry.insert(0, self.addition)
                    self.addition = 0
                    self.plus = False
                except ValueError:
                    self.entry.delete(0, END)
                    self.addition = self.addition + float(number1)
                    self.entry.insert(0, self.addition)
                    self.addition = 0
                    self.plus = False

            if self.minus1:
                try:
                    number1 = self.entry.get()
                    self.entry.delete(0, END)
                    self.minus = self.minus - int(number1)
                    self.entry.insert(0, self.minus)
                    self.minus = 0
                    self.minus1 = False
                except ValueError:
                    self.entry.delete(0, END)
                    self.minus = self.minus - float(number1)
                    self.entry.insert(0, self.minus)
                    self.minus = 0
                    self.minus1 = False

            if self.multiply1:
                try:
                    number1 = self.entry.get()
                    self.entry.delete(0, END)
                    self.multiply = self.multiply * int(number1)
                    self.entry.insert(0, self.multiply)
                    self.multiply = 0
                    self.multiply1 = False
                except ValueError:
                    self.entry.delete(0, END)
                    self.multiply = self.multiply * float(number1)
                    self.entry.insert(0, self.multiply)
                    self.multiply = 0
                    self.multiply1 = False

            if self.divide1:
                try:
                    number1 = self.entry.get()
                    self.entry.delete(0, END)
                    self.divide = self.divide / int(number1)
                    self.entry.insert(0, self.divide)
                    self.divide = 0
                    self.divide1 = False
                except ValueError:
                    self.entry.delete(0, END)
                    self.divide = self.divide / float(number1)
                    self.entry.insert(0, self.divide)
                    self.divide = 0
                    self.divide1 = False
        
        #Calculator entry display
        self.entry = Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        #Calculator buttons
        self.operator1 = Button(master, text="√", padx=20, pady=10, command=lambda: square_root(self))
        self.operator2 = Button(master, text=" x2", padx=20, pady=10, command=lambda: square(self))
        self.operator3 = Button(master, text="C", padx=20, pady=10, command=lambda: clear(self))
        self.operator4 = Button(master, text="⌫", padx=20, pady=10, command=lambda: back(self))

        self.operator1.grid(row=1, column=0)
        self.operator2.grid(row=1, column=1)
        self.operator3.grid(row=1, column=2)
        self.operator4.grid(row=1, column=3)


        self.button1 = Button(master, text="7", padx=21, pady=10, command=lambda: button_click(self, 7))
        self.button2 = Button(master, text="8", padx=24, pady=10, command=lambda: button_click(self, 8))
        self.button3 = Button(master, text="9", padx=21, pady=10, command=lambda: button_click(self, 9))
        self.button4 = Button(master, text="÷", padx=24, pady=10, command=lambda: divide(self))

        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=2, column=3)


        self.button5 = Button(master, text="4", padx=21, pady=10, command=lambda: button_click(self, 4))
        self.button6 = Button(master, text="5", padx=24, pady=10, command=lambda: button_click(self, 5))
        self.button7 = Button(master, text="6", padx=21, pady=10, command=lambda: button_click(self, 6))
        self.button8 = Button(master, text="X", padx=25, pady=10, command=lambda: multiply(self))

        self.button5.grid(row=3, column=0)
        self.button6.grid(row=3, column=1)
        self.button7.grid(row=3, column=2)
        self.button8.grid(row=3, column=3)


        self.button9 = Button(master, text="1", padx=21, pady=10, command=lambda: button_click(self, 1))
        self.button10 = Button(master, text="2", padx=24, pady=10, command=lambda: button_click(self, 2))
        self.button11 = Button(master, text="3", padx=21, pady=10, command=lambda: button_click(self, 3))
        self.button12 = Button(master, text="-", padx=25, pady=10, command=lambda: minus(self))

        self.button9.grid(row=4, column=0)
        self.button10.grid(row=4, column=1)
        self.button11.grid(row=4, column=2)
        self.button12.grid(row=4, column=3)


        self.button13 = Button(master, text="0", padx=21, pady=10, command=lambda: button_click(self, 0))
        self.button14 = Button(master, text=".", padx=24, pady=10, command=lambda: button_click(self, "."))
        self.button15 = Button(master, text="+", padx=21, pady=10, command=lambda: add(self))
        self.button16 = Button(master, text="=", padx=24, pady=10, command=lambda: equal(self))

        self.button13.grid(row=5, column=0)
        self.button14.grid(row=5, column=1)
        self.button15.grid(row=5, column=2)
        self.button16.grid(row=5, column=3)


root = Tk()
window = Calculator(root)
root.mainloop()