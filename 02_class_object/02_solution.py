import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
    
    def getArea(self):
        result = math.pi * (self.radius**2)
        return result
        
    def getCircumference(self):
        result = (2 * math.pi) * self.radius
        return result

c1 = Circle(2)
print(c1.getRadius())
print(c1.getArea())
print(c1.getCircumference())

