# Leap year is divisible by 4, but not 100 unless it is also divisible by 400.

year = 2024
# (year % 4 == 0)
# (year % 100 != 0)
# (year % 400 == 0)

if (year % 400 == 0) and (year % 100 != 0) or (year % 4 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# Triangle classifier

side1 = int(input("Enter side1"))
side2 = int(input("Enter side2"))
side3 = int(input("Enter side3"))

if side1 == side2 == side3:
    print("Equitorial triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Iso triangle")
else:
    print("scalene")



