# Encapsulation
# Example to show Public, Private, Protected variables
class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"

    def __private_method(self):
        print("Private")

    def printName(self):
        self.__private_method()
        if self.__private_var == "pass@123":
            print("Accessing private variable via class function")
        else:
            print("Can't access private member from outside")


alto = Car()
alto.name = "XUV"
print(alto.name)
# alto._protected_var -> Not allowed
# alto.__private_var -> Not allowed
# alto.__private_method -> Not allowed

alto.printName()