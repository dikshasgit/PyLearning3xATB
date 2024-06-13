# Task - Fibonacci series and Factorial
# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24


# num = int(input("Enter the number"))
# result = 1
# while(num>0):
#     result = result*num
#     num = num-1
#
# print(f"factorial of {num} is {result}")

# 4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 1, 2, 3, 5, 8, 13

num1 = 0
num2 = 1
nextNum = num2
limit = int(input("Enter the limit"))

print(num1, end=' ')
print(num2, end=' ')

while(nextNum<=limit):
    print(nextNum, end=' ')
    num1, num2 = num2, nextNum
    nextNum = num1 + num2