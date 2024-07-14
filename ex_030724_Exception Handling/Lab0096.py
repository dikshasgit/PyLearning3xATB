# Custom exception
class MyCustomException(Exception):# for making own exception we need to inherate exception in class
    def __init__(self,message):
        self.message=message + "loL"
        super().__init__(message)# super is calling the parent constructor
balance =100
withdraw= int(input("Enter the number"))
if  withdraw >balance:
    raise MyCustomException("balance is low")
else:
    print("remaining balance", (balance-withdraw) )


    class Parent:

        def __init__(self):
            print("i am snigdha")


    class Son(Parent):
        def __init__(self):
            super().__init__()


    S = Son()  # when we create object the constructor will be called


    def main():
        print("hello main")


    main()