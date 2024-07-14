# Filter in Python
# The filter() function is a built-in function
# which allows you to filter elements in the list, tuple, set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(num):
    return num % 2 == 0


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))

