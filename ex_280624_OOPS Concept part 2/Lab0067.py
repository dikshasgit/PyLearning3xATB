# Encapsulation
# Here password can be changed from outside the class as password is public, this should not be allowed
class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an object is created")


xuv = Car()
print(xuv.password)
xuv.password = "456"
print(xuv.password)



