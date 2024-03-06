class Queue:
    def __init__(self):
        self.items = []
        self.item_count = 0

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, data):
        self.items.append(data)
        self.item_count +=1 
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
            self.item_count -=1 
        else:
            raise IndexError ("Queue Underflow")
    
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError ("Queue Underflow")
    
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError ("Queue Underflow")
        
    def size(self):
        return self.item_count
    

q1 = Queue()
try:
    print(q1.get_front() )
except IndexError as e:
    print(e.args[0])    

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("Front:", q1.get_front(), "Rear:", q1.get_rear())
try: 
    q1.dequeue()
    print("Queue has now", q1.size(), "elements")
except ImportError as e:
    print(e.args[0])
