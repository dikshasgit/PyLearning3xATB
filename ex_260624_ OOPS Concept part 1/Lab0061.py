# Class Dog

class dog:
    name = None
    size = None
    colour = None

    def sleep(self):
        print("Sleeping")


dog1 = dog()
dog2 = dog()
dog1.name = "Chow"
dog2.size = "Small"
dog2.sleep()
print(dog1.name)
print(dog2.size)