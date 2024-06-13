# Task #2

# 1. Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
# 2. Create a program that takes two numbers as input and prints whether the first number is greater than, less than,
# or equal to the second number.

# 2.
num1 = 5
num2 = 6


def compare_numbers(num1, num2):
    if num1 > num2:
        return "First no is greater than second no."
    elif num1 < num2:
        return "First no. is less than second no."
    else:
        return "First no is equal to second"


num1 = float(input("Enter the first no"))

num2 = float(input("Enter the second no."))
result = compare_numbers(num1, num2)
print(result)
print(input(num1))


# 1.
def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area


radius = float(input("Enter the radius of circle:"))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius{radius} is {area}")
