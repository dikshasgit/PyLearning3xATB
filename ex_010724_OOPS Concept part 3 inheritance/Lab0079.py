#multiple
class A:
    def method(self):
        print("i am calling method a")

class B:
    def method(self):
        print("this is a method b")

class c(A,B): # whatever we select first that's object will only be called
    # def methodc(self):
    #     print("this is a c clas method")
        pass


Object_rej = c()
print(Object_rej.method())# caling a method becuse a is first called



