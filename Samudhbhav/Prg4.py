# Contents in stack1.py :
# class Stack:
#    def __init__(self):
#        self.items = []

#    def isEmpty(self):              # Returns True if empty else False
#        return self.items == []
        
#    def push(self, item):           # Appends/pushes to the end of the list
#        self.items.append(item)

#    def insert(self,index, item):   # Inserts at any desired index in list
#        self.items.insert(index,item)

#    def pop(self):                  # Pops element out from the end
#        return self.items.pop()

#    def peek(self):                 # Peeks to the last element added
#        return self.items[len(self.items)-1]

#    def size(self):
#        return len(self.items)

from stack1 import Stack

s = Stack()

print(s.isEmpty()) 
s.push(4)            
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
s.insert(2,'cat')
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
