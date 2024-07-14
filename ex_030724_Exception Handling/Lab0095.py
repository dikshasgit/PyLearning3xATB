class XYZ:
    def f1(self):
        try:
            a = int(input("Enter a number\n "))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)
        finally:
            print("FINALLY: Any how I will be printed")



x = XYZ()
x.f1()



# Custom exception
class MyCustomException(Exception):# for making own exception we need to inherate exception in class
    def __init__(self,message):
        self.message=message +"low"
        super().__init__(message)# super is calling the parent constructor
balance =100
withdraw= int(input("Enter the number"))
if  withdraw >balance:
    raise Exception("balance is low")
else:
    print("remaining balance", (balance-withdraw) )