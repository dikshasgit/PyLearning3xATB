#multiple inheritance

class father:

    def father_method(self):
        return "50000"
    def home(self):
        print("this is my house, i bought it")
class Mother:
    def mother_money(self):
        return "2"

    def home(self):
        print("This is my house, mother bought it")

class Son(Mother, father):
    def home(self): # loacl has a prefrence
        print("this is son's house")

#java- diamonde problem- java
#python multiple inheritance

son=Son()
son.father_method()
son.mother_money()
print(son.home()) # method resolution, it will call first local method if all have same method name, son doesnt have same method then it will show
# who's class is  inherited first.