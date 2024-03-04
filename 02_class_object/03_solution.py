class Rectangle:
    def __init__(self, name=None, length=None, breadth=None):
        self.name = name
        self.length = length
        self.breadth = breadth
    
    def setDimention(self, name, length, breadth):
        self.name = name
        self.length = length
        self.breadth = breadth

    def showDimention(self):
        print("Dimentions of", self.name, "are", self.length, "x", self.breadth)

    def getArea(self):
        result = self.length * self.breadth
        return result
    
r1 = Rectangle("r1", 3, 6)
r1.showDimention()
print(r1.getArea())

r2 = Rectangle()
r2.setDimention("r2",5,10)
r2.showDimention()
print(r2.getArea())