#hierarchical -Inheritance
# father -Multiple childrend

class Father:
    def Bhk1(self):
        print("i have 1bhk")

class Promod(Father):
    def Bhk2(self):
        print("i have 2 bhk")

class lucky(Father):
    def Bhk3(self):
        print("i have 3bhk")

class Amit(Father):
    def nohouse(self):
        print("i dont have house")


Promde=Promod()
Promde.Bhk2()
Promde.Bhk1()


Lucky=lucky()
Lucky.Bhk3()
Lucky.Bhk1()

amit=Amit()
amit.nohouse()
amit.Bhk1()