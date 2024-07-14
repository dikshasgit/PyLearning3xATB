#indentationError
#  print("dad")#indentationError

# result =5+"5" # TypeError: unsupported operand type(s)for +: 'int' and 'str'

# int("snigdha") # ValueError: invalid literal for int() with base 10: 'snigdha'

# print(undefin_variable) # NameError: name 'undefin_variable' is not defined


# my_list =[1,2,3]
# print(my_list[3])  #IndexError: list index out of range

# my_dict = {"a":1 , "b":2}
# print(my_dict["c"])  #KeyError: 'c'

# result = 10/0     # Zero Division Error

#import non_existent_module    #ModuleNotFoundError: No module named 'non_existent_module'


try:
    # while True print("hello")
    a = 10/0
except Exception as e:# e variable, as is
    print(e)


# Errors are something which are difficult to recover
# Errors are more severe issues that typically prevent the program from running
# impossible to handle, Syntax, Indentation



# Exception(error) -> can be handled
# Exceptions are events that occur during the execution of a program that disrupts the normal flow of instructions
# Program recover can possible