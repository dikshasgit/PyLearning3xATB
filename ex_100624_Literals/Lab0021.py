# Arithmetic Operators
# +,-,*,/, %
a = 180
b = 90
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # Float - Why Python is smart - div

print(a % b)
print(10 ** 2)
r = pow(10, 2)
print(r)

# Modulus - Operator -> Reminder
# 90 | 180 | 2
#    | 180 |
#    |   0 |
#
print(64 % 10)
print(87 // 10) # Quetion
print(87 / 10) # Float
print(87 // 10.0) # Float

# Logical Operator - bool
x = 10
y = 20
print(x > y)
print(x < y)

a = 10
b = 10
print(a >= b)  # 10 > 10 or 10 = 10
print(a == b)  # 10 > 10 or 10 = 10
print(not a)
# Or Gate

f = False
t = True
print(f and t)
print(f or t) # Truth Table of or

x = 10
y = 20

result = (x != y) # 10 not equal 20 -> True #!-not operator
print(result)

