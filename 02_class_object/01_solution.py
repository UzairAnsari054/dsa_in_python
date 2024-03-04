class Person:
    def __init__(self, name, age):   #2Internally... (def __init__(p1, "uzair", 25)
        self.name = name             # p1.name = "uzair"
        self.age = age               # p1.age = 25

    def show(self):
        print("Person name is", self.name, "& age is", self.age)

p1 = Person("uzair", 25)             #1Internally... (p1 = Person(p1, "uzair", 25)
                                                     #(def __init__(p1, "uzair", 25)
p1.show()                            #3Internally... p1.show(p1)