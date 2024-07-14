# hybrid -inhertance, we can mix different type of heriache, single, multilevel, multiple
class A:
 def methodA(self):
     return "method a"

class B(A):
 def methodB(self):
     return "method b"

class C(A):
 def methodc(self):
     return "method c"

class D(B,C):   #multiple, #multilevel
 def methodD(self):
     return "method d"

d=D()
print(d.methodA())
print(d.methodc())
print(d.methodB())
print(d.methodD())