class Node:
    def __init__(self, item=None, priority=None, next=None):
        self.item = item
        self.priority = priority
        self.next = next

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None
    
    def push(self, data, priority):
        n = Node(data, priority)
        if not self.start or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            n.next = temp.next
            temp.next = n
        self.item_count += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        else:
            data =  self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        
    def size(self):
        return self.item_count
    
p1 = PriorityQueue()
p1.push("Amit", 4)
p1.push("Arjun", 7)
p1.push("Ashima", 2)
p1.push("Agrah", 5)
p1.push("Anant", 8)
p1.push("Ambika", 1)

while not p1.is_empty():
    print(p1.pop())




