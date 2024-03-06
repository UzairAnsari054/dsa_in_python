class Stack(list):
    def is_empty(self):            # self, stack ke object ko reresent kar raha h aur stack ki parent class h list
        return len(self) == 0      # toh me self likh kr list access kar skta hu
    
    def push(self, data):
        self.append(data)    # self. lagae stack ke members ko bhi access kar skte ho aur list ke members ko be access kar skte ho

    def pop(self):
        if not self.is_empty:
            super.pop()         # here, super keyword ensures that parent class i.e List's pop() get called & not the pop function of Stack, because then due to overriding it'll end-up in recurrsion
        else:
            raise IndexError("Stack is Empty")
    
    def peek(self):
        if not self.is_empty():      # here, self is basically list 
            return self[-1]
        else:
            raise IndexError("Stack is Empty")
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No Attribute 'insert" in Stack)   # Doing this will allows us to ensure that insert() of list never gets called. This is overriding
    
s1 = Stack()
# s1.insert(1, 10)
s1.push(10)
s1.push(20)
s1.push(30)
print("top value:", s1.peek())
