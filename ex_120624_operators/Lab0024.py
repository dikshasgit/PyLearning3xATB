# Operators - Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# 1. Arthmetic operators-are used with numeric values to perform common mathematical operations
# Operators - (+) , (-), (*), (/), (%), (**)-exponential , // - floor division
x = 5
y = 3
#print(x + y)
#print(x - y)
#print(x * y)
#print(x % y)
#print(x ** y)
#print(x // y)

# 2. Assignment operator-are used to assign values to variables:
# operators- (=) - x = 5 , (+=)- x += 3, (-=)- x-=3 ,x %= 3(Remender), x //= 3(quetion), #BODMAS
# x &= 3, x |= 3 , x ^= 3, x <<=3, x>>=3, x := 3
x = 5
x= x += 3
print(x)

x= x /=3
print(x)
x = x *= 3
print(x)
x = x -= 3
print(x)

x = ^= 3
print(x)
x = x >>=3
x = <<=3
print(x)

print(x:=3)
x = print(x)
