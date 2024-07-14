#Encapsulatioin
#Polymorphism
#Constructor
#clas
#object
#self, super
#private, __protect, _private

# Abstraction-oops
#Abstarction- hiding the detaisl and showing what is required

from abc import ABC, abstractmethod
class Animals(ABC):
    def __init__(self,name):
        self.name=name


    @abstractmethod  #incomplete method/function given by Animal class, anyone who is
    def sounds(self):
        pass

class Dog(Animals):
    def sounds(self):
        return "Bark"


class Cat(Animals):
    def sounds(self):
        return "meow"

D=Dog("brownie")
print(D.sounds())
C=Cat("bluely")
print(C.sounds())