# Task-1
# 1.Explain the difference between the = operator and the == operator in Python.
# 2.What does the ** operator do in Python, and how is it used?
# 3.What does the ^ operator do in Python, and in what context is it commonly used?

# a. == - is a camparison operator ,used it to campare 2 values

x = 5
y = 3
print(x == y)

# b = - is a assignment operator , are used to assign values to variables

x = 5
print(x)

# c ** - is a arthemetic operator called exponential operator ,
#       used with numeric value to perform common mathmatical operations

x = 2
y = 5
print(x ** y)  # same as 2*2*2*2*2

# d ^ - is bitwise operator called XOR, are used to compare binary numbers
# set each bit to 1 if only one of two bits is 1

print(6 ^ 3)
"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to
 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
