from .stack import Stack
from tkinter import END
import operator

stack = Stack()

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def evaluate(entry_field):
    operand2 = int(stack.pop())
    operator = stack.pop()
    operand1 = int(stack.pop())

    result = ops[operator](operand1, operand2)

    entry_field.insert(0, result)


def add(entry_field):
    num = entry_field.get()
    stack.push(num)
    entry_field.delete(0, END)

    if stack.size() < 3:
        stack.push('+')
    else:
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


def square_root():
    pass


def square():
    pass
