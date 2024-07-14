# method overloading- python doesn't support method overloading
# in tradition sense

class Mathutil:


    def add(self,x,y,z=9):
        return x+y+z


math=Mathutil()
opt= math.add(7,0)
opt1=math.add(5,12)
print(math.add(3,4,7))
print(opt)
print(opt1)


