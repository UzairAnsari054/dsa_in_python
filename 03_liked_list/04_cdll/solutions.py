class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev        
            self.start.prev.next = n
            self.start.prev = n     
        self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            n.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start   
        if temp is None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next

        while temp != self.start:     # Here temp has 2nd node 
            if temp.item == data:
                return temp
            temp = temp.next
        return None
            
    def insert_after(self, temp, data):   
        if temp is not None:
            n = Node(item = data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    
    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start  = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
            
    def delet_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start  = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
            
    def delete_item(self, data):
        if self.start is not None:
            temp = self.start
            if temp.item == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp != self.start:
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next

    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while temp != self.start:
                print(temp.item, end=' ')
                temp = temp.next
        
    def __iter__(self):
        return CdllIterator(self.start)
        
        

class CdllIterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):             # yeh rokna kab chahiye
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:    # 1st cycle complete hone ke baad, 2nd cycle shuru hote hi rok dena h. Jab self. current 1st node ko point kare (1st condition) and self.count me 1 ho (2nd condition) to stop karna h iteration. Ab 1st cycle me self.current 1st node ko to point krega hi par tab self.count me 1 nhi 0 hoga, but second round shuru hone se phele ham self.count me 1 rakh denge
            raise StopIteration
        else:
            self.count = 1
            data = self.current.item
            self.current = self.current.next
            return data

mylist = CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30), 35)
for x in mylist:
    print(x, end=' ')
