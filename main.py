# Created by Ayotomiwa Adekunle

from tkinter import Entry, Button, Tk, END
from utils.arithmetic import *


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.resizable(False, False)

        # Calculator entry display
        self.entry = Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Calculator buttons
        self.operator1 = Button(master, text="√", padx=20,
                                pady=10, command=lambda: square_root())
        self.operator2 = Button(
            master, text=" x2", padx=20, pady=10, command=lambda: square())
        self.operator3 = Button(master, text="C", padx=20,
                                pady=10, command=lambda: self.clear())
        self.operator4 = Button(master, text="⌫", padx=20,
                                pady=10, command=lambda: self.back())

        self.operator1.grid(row=1, column=0)
        self.operator2.grid(row=1, column=1)
        self.operator3.grid(row=1, column=2)
        self.operator4.grid(row=1, column=3)

        self.button1 = Button(master, text="7", padx=21,
                              pady=10, command=lambda: self.button_click(7))
        self.button2 = Button(master, text="8", padx=24,
                              pady=10, command=lambda: self.button_click(8))
        self.button3 = Button(master, text="9", padx=21,
                              pady=10, command=lambda: self.button_click(9))
        self.button4 = Button(master, text="÷", padx=24,
                              pady=10, command=lambda: divide())

        self.button1.grid(row=2, column=0)
        self.button2.grid(row=2, column=1)
        self.button3.grid(row=2, column=2)
        self.button4.grid(row=2, column=3)

        self.button5 = Button(master, text="4", padx=21,
                              pady=10, command=lambda: self.button_click(4))
        self.button6 = Button(master, text="5", padx=24,
                              pady=10, command=lambda: self.button_click(5))
        self.button7 = Button(master, text="6", padx=21,
                              pady=10, command=lambda: self.button_click(6))
        self.button8 = Button(master, text="X", padx=25,
                              pady=10, command=lambda: multiply())

        self.button5.grid(row=3, column=0)
        self.button6.grid(row=3, column=1)
        self.button7.grid(row=3, column=2)
        self.button8.grid(row=3, column=3)

        self.button9 = Button(master, text="1", padx=21,
                              pady=10, command=lambda: self.button_click(1))
        self.button10 = Button(master, text="2", padx=24,
                               pady=10, command=lambda: self.button_click(2))
        self.button11 = Button(master, text="3", padx=21,
                               pady=10, command=lambda: self.button_click(3))
        self.button12 = Button(master, text="-", padx=25,
                               pady=10, command=lambda: minus())

        self.button9.grid(row=4, column=0)
        self.button10.grid(row=4, column=1)
        self.button11.grid(row=4, column=2)
        self.button12.grid(row=4, column=3)

        self.button13 = Button(master, text="0", padx=21,
                               pady=10, command=lambda: self.button_click(0))
        self.button14 = Button(master, text=".", padx=24,
                               pady=10, command=lambda: self.button_click("."))
        self.button15 = Button(master, text="+", padx=21,
                               pady=10, command=lambda: add())
        self.button16 = Button(master, text="=", padx=24,
                               pady=10, command=lambda: equal())

        self.button13.grid(row=5, column=0)
        self.button14.grid(row=5, column=1)
        self.button15.grid(row=5, column=2)
        self.button16.grid(row=5, column=3)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))

        # Checks if a number is pressed during an operation
        if self.but_press == True:
            self.entry.delete(0, END)
            self.entry.insert(0, str(number))
            self.but_press = False

    def clear(self):
        self.entry.delete(0, END)
        # reset values
        self.addition = 0
        self.minus = 0
        self.multiply = 0
        self.divide = 0

    def back(self):
        current = self.entry.get()
        display = current[0:-1]
        self.entry.delete(0, END)
        self.entry.insert(0, display)

    def equal(self):
        pass


root = Tk()
window = Calculator(root)
root.mainloop()
