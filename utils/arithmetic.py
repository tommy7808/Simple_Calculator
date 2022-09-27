from .stack import Stack
from tkinter import END
from math import sqrt

import operator

stack = Stack()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def evaluate(entry_field, equal=False):
    # Check if equal button has been pressed
    if equal:
        num = entry_field.get()
        stack.push(num)
        entry_field.delete(0, END)

    operand2 = float(stack.pop())
    operator = stack.pop()
    operand1 = float(stack.pop())

    result = ops[operator](operand1, operand2)

    entry_field.insert(0, result)


def add(entry_field):
    num = entry_field.get()
    stack.push(num)
    entry_field.delete(0, END)

    if stack.size() < 3:
        stack.push('+')
    else:
        # If stack is full evaluate
        evaluate(entry_field)


def minus(entry_field):
    num = entry_field.get()
    stack.push(num)
    entry_field.delete(0, END)

    if stack.size() < 3:
        stack.push('-')
    else:
        evaluate(entry_field)


def multiply(entry_field):
    num = entry_field.get()
    stack.push(num)
    entry_field.delete(0, END)

    if stack.size() < 3:
        stack.push('*')
    else:
        evaluate(entry_field)


def divide(entry_field):
    num = entry_field.get()
    stack.push(num)
    entry_field.delete(0, END)

    if stack.size() < 3:
        stack.push('/')
    else:
        evaluate(entry_field)


def square_root(entry_field):
    num = entry_field.get()
    entry_field.delete(0, END)

    num = sqrt(float(num))

    entry_field.insert(0, num)


def square(entry_field):
    num = entry_field.get()
    entry_field.delete(0, END)

    num = float(num) ** 2

    entry_field.insert(0, num)


def equal(entry_field):
    if stack.size() == 2:
        evaluate(entry_field, True)
