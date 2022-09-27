# Basic stack data structure implementation

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)
