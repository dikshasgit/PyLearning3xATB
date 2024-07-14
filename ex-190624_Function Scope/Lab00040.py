# Lambda expression is a one line function
# It is used to define a function in one line

def double(x):
    return x * 2

result = double(5)
print(result)  # Output: 10

# using lambda expression same function written as
double = lambda x: x * 2
result = double(5)
print(result)  # Output: 10


# Adding three numbers
def sum_three(a, b, c):
    return a + b + c


sum = sum_three(1, 2, 3)
print(sum)  # Output: 6

# Using a lambda expression
sum_three = lambda a, b, c: a + b + c
sum = sum_three(1, 2, 3)
print(sum)  # Output: 6


# Adding two numbers using a lambda expression
add = lambda a, b: a + b
sum = print(add(5, 3))

# Finding the maximum of two numbers using a lambda expression
maximum = lambda a, b: max(a, b)
result = print(maximum(10, 20))