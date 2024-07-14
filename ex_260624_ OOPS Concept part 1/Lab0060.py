# Class

class person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviour
    def talk(self):                 # No args, no return
        print("I can talk")

    def walk(self):                 # No args, with return
        print("I can walk")
        return "Hi Mangesh"

    def sleep(self, name):          # 1 arg, no return
        print("I am sleep method")
        print(name, "Please sleep")

    def add(self, a, b):          # 1 arg, with return
        return a+b


mangesh = person()
mangesh.name = "Mangesh Dave"
print(mangesh.name)
print("Method - 1")
mangesh.talk()
print("Method - 2")
new_str = mangesh.walk()
print(new_str)
print("Method - 3")
mangesh.sleep("Dave")
print("Method - 4")
sum2 = mangesh.add(3, 4)
print("Addition is = ", sum2)