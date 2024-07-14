# abstract we use to force something
from abc import ABC, abstractmethod
class Pyth(ABC):

    #abstractmethod
    def payFee(self):
        pass


    def enroll(self):
        print("enrolled")

class Shubham(Pyth):

    def payFee(self):
        print("payed")


S=Shubham()
print(S.payFee())
print(S.enroll())