# Abstract method
from abc import ABC, abstractmethod # module

class ATB(ABC):
    def enroll(self):
        print("if you are enrolled")

    @abstractmethod
    def performtask1(self):
        pass

    @abstractmethod
    def performtask2(self):
        pass
class Amit(ATB):
    def performtask1(self):
        print("completed")
        return "done"


    def performtask2(self):
        print("uncompleted")
        return "notdone"

A=Amit()
print(A.performtask1())
print(A.performtask2())