# Ternary Operator
Diksha_marks = 97
amit_marks = 68

#   x > y -> do something - print("Diksha")
# y > x -> do something else -> print("amit)
print("Diksha is winner" if Diksha_marks > amit_marks else "amit is winner")


if Diksha_marks > amit_marks:
    print("Diksha is the winner")
else:
    print("Amit is the winner")


# Program - Calculate the area of circle.
# input -> radius
# output -> area
import math

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("Enter the radius\n"))
print(math.pi)
area = math.pi*(radius**2)
area2 = math.pi*(math.pow(radius,2))
print(area)
print(area2)

