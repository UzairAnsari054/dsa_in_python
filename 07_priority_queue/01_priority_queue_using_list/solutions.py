class PriorityQueue:               # In priority queue data is stoted in the form of tuple, eg. list = (93,0), (33,1), (923,2)
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1]<=priority:
            index += 1
        self.items.insert(index, (data, priority))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority queue empty")
        else:
            return self.items.pop(0)[0]

    def size(self):
        return len(self.items)
    
p1 = PriorityQueue()
p1.push("Amit", 4)
p1.push("Arjun", 7)
p1.push("Ashima", 2)
p1.push("Agrah", 5)
p1.push("Anant", 8)
p1.push("Ambika", 1)

while not p1.is_empty():
    print(p1.pop())

            
