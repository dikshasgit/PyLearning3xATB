#overridding
class Father:
    def home(self):
        print("1bhk")

class Son(Father):
    def home(self):
        super().home()# super will only give the access immediate class method only not grand father method
        print("3bhk")
        print("no house")

F=Father()
S=Son()
print(S.home())


