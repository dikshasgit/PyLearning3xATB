# Recursive function

def sum_of_digit(n):
    # Base Case
    if n < 10:
        return n
    # Recursive Case
    else:
        return n % 10 + sum_of_digit(n // 10)


print(sum_of_digit(12345))


# Recursive function

def factorial(n):
    # Base case
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))