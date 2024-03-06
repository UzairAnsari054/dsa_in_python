class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
         n = Node(item=data, next=self.start)
         if not self.is_empty:
             self.start.prev = n
         self.start = n

    def insert_at_last(self, data):
        temp = self.start
        if temp is not None:
            while temp.next is not None:
                temp = temp.next
        
        n = Node(prev=temp, item=data)
        if temp is not None:
            temp.next = n
        else:
            self.start = n
        

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
        
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(prev=temp, item=data, next=temp.next)
            if(temp.next is not None):
                temp.next.prev = n
            temp.next = n

    def print_all(self):
        temp = self.start
        while temp is not None: 
            print(temp.item, end=' ')
            temp = temp.next
    
    def deleteFirst(self):
        if self.start is None:
            pass
        else:
            self.start.next.prev = None
            self.start = self.start.next
    
    def deleteLast(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
        
    def delete_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else: 
                        self.start = temp.next
                    break
                temp = temp.next
                

    def __iter__(self):
        return DllIterator(self.start)



class DllIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
    

myList = DLL()
myList.insert_at_start(10)
myList.insert_at_last(20)
myList.insert_after(myList.search(10), 15)
# for x in myList:
#     print(x, end= ' ')
myList.print_all()
print()
# myList.deleteLast()
myList.delete_item(20)
myList.print_all()