# Class Dog - Constructor

class dog:
    name = None
    size = None
    colour = None

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def sleep(self):
        print("Sleeping")


dog1 = dog("Chow", "Small")
dog2 = dog("Mow", "Big")
print(dog1.name)
print(dog1.size)
dog2.sleep()
print(dog2.name)
print(dog2.size)