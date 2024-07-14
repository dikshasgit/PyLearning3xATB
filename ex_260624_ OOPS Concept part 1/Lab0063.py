# Class - Calculator

class calc:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc1 = calc()
addition = calc1.add(20, 10)
print(addition)
subtraction = calc1.sub(20, 10)
print(subtraction)
multiplication = calc1.mul(20, 10)
print(multiplication)
division = calc1.div(20, 10)
print(division)