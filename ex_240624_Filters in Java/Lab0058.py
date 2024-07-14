# Filter in Python
# The filter() function is a built-in function
# which allows you to filter elements in the list, tuple, set

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_greater_than_5(num):
    return num > 5


new_numbers = filter(is_greater_than_5, numbers)
print(list(new_numbers))