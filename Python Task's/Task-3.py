# Program to Calculate the Square and Cube of a Number

def calculate_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube


# ex-
number = float(input('Enter the number:'))
square, cube = calculate_square_and_cube(number)
print(f"The square of {number} is {square}")
print(f"The cube of {number} is {cube}")

def calculate_square_and_cube(number):
     square = number ** 2
     cube = number ** 3
     return square,cube

number = float(input("Enter the no:"))
square,cube = calculate_square_and_cube(number)
print(f"The square of {number} is {square}")
print(f"The cube of{number} is {cube}")




