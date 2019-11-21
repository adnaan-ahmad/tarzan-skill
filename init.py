class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return "{} sings {} and his age is {}".format(self.name,song,self.age)

    def dance(self,name):
        return "{} is dancing".format(name)

obj1=Parrot('mithu',3)
print(obj1.sing("tum hi ho"))
print(obj1.dance('adnan'))