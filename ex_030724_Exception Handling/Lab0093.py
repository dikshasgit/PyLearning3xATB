# try, except and finally
#catch doesnt exist in python, we have except
try:
    num1=int(input("enter a number 1 \n"))
    num2=int(input("enter a number  2\n"))
    result=num1/num2
    print(result)
except ValueError as ve:
    print(ve)

except ZeroDivisionError as ze:
    print(ze)
else:
    print(f'Result is {result}')

finally:
    print("i will be executed any how")