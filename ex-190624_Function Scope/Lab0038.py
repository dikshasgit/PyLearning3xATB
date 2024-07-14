#Function scope

a=3 #global varialbe
def f1():
    print(a)
f1()

def my_function():
    x = 10  # Local variable
    local_var = 20
    print("Inside the function")
    print(x)
    print(local_var)


# print(x) # name 'x' is not defined
my_function()


def outer_function():
      var1= 31
      def inner_function():
          print(var1)

      inner_function()
outer_function()


