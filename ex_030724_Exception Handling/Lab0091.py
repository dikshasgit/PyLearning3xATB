print("-----start of the program-------")
try:
    a = int(input("enter in the number \n"))
    b = int(input("enter the second num \n"))
    c = a * b  # if user taken 0 ZeroDivisionError: division by zero
    print("result multiple num is", c)
except Exception as e:
    print(e)
    print("Please enter the integer value only")


print("-----end of the program------")



#try
#  # try this code if some errors
#except:
#  #execute me if try has some error