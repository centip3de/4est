
class Stack():
    def __init__(self):
        self.mem = []

    def push(self, data):
        self.mem.append(data)

    def pop(self):
        return self.mem.pop()

    def peek(self):
        return self.mem[-1]

class AST():
    def __init__(self):
        pass
