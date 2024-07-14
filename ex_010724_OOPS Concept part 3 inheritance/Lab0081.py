#multiple return function

def multiple_return_fun():
    return 99,"Promode",True

print(multiple_return_fun())


class GF:
    def car(self):
        return"old car"

class F(GF):
    def car(self):
        return "aulto"

class S(F):
    def car(self):
        return "lambogirni"

son=S()
print(son.car())
print(son.car())
gf=GF()
print(gf.car())