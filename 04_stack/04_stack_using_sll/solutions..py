from Assignment_SLL import *

class Stack:
    def __init__(self):
        self.mySll = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.mySll.is_empty()  # also we can do, return self.item_count
    
    def push(self, data):
        self.mySll.insert_at_start(data)
        self.item_count += 1

    def pop(self):
        if not self.is_empty():
            self.mySll.delete_first()
            self.item_count -= 1
        
    def peek(self):
        if not self.is_empty():
            return self.mySll.start.item
        
    def size(self):
        return self.item_count
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("Top element is:", s.peek())
s.pop()
print("Top element is:", s.peek())

        