class Animal:
    def __init__(self):
        print("animal created")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("dog created")

    def whoAmI(self):
        print("dog")

    def eat(self):
        print("DRINK")
        
d=Dog()
d.whoAmI()
d.eat()