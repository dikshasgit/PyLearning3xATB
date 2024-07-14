#multilevel heritance
class Grandfather:
    keytothegold= "4kg"
    def grandfather_method(self):
        print("this is my grandfather method")

class Parent(Grandfather):
    def parent_method(self):
        print("this is my parent method")

class child(Parent):
    brought= "Macbook"
    def child_method(self):
        print("this is child method")

parent=Parent()
parent.parent_method()
parent.grandfather_method()
print(parent.keytothegold)

Child=child()
Child.child_method()
print(Child.brought)
Child.parent_method()
Child.grandfather_method()
print(child.keytothegold)