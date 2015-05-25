# Samudhbhav/stack1.py
# Contents of stack1.py :
# Used in Prg4.py
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)

    def insert(self,index, item):
        self.items.insert(index,item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
