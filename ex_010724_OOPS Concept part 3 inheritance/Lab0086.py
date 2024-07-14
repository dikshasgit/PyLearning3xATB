#Abstract

from abc import ABC, abstractmethod
class Father(ABC):
    def __init__(self,name):
        self.name=name


    #abstractmethod  #incomplete method/function given by Animal class, anyone who is
    def loan(self):
        pass

class Promode(Father):
    def loan(self):  #we have to use loan abstract method, forceful method
        print("loan given")


class Cat(Father):
    def loan(self):
        return "meow"

P=Promode("brownie")
print(P.loan())
C=Cat("bluely")
print(C.loan())