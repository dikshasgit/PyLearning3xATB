# polymorphism
#polymorphism allows the object of different
# different class to be trated as
#object of common  superclass

#Promode-mentor,husband,son,brother
#object- method--> mother-sister,wife,

#method overriding


class shape:
    def area(self):
        print("area of the shape")
class circle(shape):
    def __int__(self,radius): # constructor
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class rectangle(shape):
    def __init__(self,length,width): #constructor
        self.length=length
        self.width=width

    def area(self):
        return self.length* self.width



S=shape()
C=circle() #
R=rectangle(5,7)
print(R.area())
print(S.area())
print(C.area())