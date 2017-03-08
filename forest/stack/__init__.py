
class Stack():
    def __init__(self):
        self.mem = []

    def push(self, data):
        self.mem.append(data)

    def pop(self):
        return self.mem.pop()

    def peek(self):
        return self.mem[-1]

    def print_stack(self):
        print("Stack: ", self.mem)

    def clear_stack(self):
        self.mem = []

    def remove_all_but_bot(self):
        bot = self.mem[0]
        self.clear_stack()
        self.push(bot)
