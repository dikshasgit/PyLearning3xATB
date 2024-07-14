# which is not common, unexpected event, sudden issue,error, an application doesnt know how to handle issue ,

# while True print("hello world") # this is syntax error
# Anexception is an event that occurs during the execution of the program
#that disturb the normal flow of the program

#while True:
#    print("hello world")


print("start")
10/0
print("end of the program")



# how to handle exception
a= int(input("enter in the number \n"))
b=int(input("enter the second num \n"))
c=a/b # if user taken 0 ZeroDivisionError: division by zero
print("result div num is",c)

# what are the problem we can face
#value error, multipleissue, why do we have to handle the exception
#ATM= sbi- insert-10k- i enter amount, money got deducted,but not received
# via ATM(we didnt received message)
# for user better experience we have to handle the issue