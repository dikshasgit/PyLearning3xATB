#Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides, determine if the triangle is equilateral
#(all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
#Use an if-else statement to classify the triangle.
# 3 Input
#side 1, side 2 and side 3
#output - Eq, Iso, Scalene -
#Eq. = side 1 == side 2 = side 3

#equilateral = all sides are equal
# isosceles = 2 sides are equal
# scalene = no sides are equal

side1 = float(input('Enter the side 1: '))
side2 = float(input('Enter the side 2: '))
side3 = float(input('Enter the side 3: '))

if (side1 == side2 == side3):
    print('Equ')
elif ((side1 == side2) | (side1 == side3) | (side2 == side3)):
    print('iso')
else:
    print('sc')




