# Pass some information to the f(n)

def greet(name):  # name -> argument
    print("Hi, How are you", name)

greet("Shirisha")
greet("Amit")
greet("123")
greet(123)


def allowed_to_attend_python_class(name, password):
    if name == "pramod":
        if password == "Yes":
            print("You are allowed to enter")
        else:
            print("Not allowed")


allowed_to_attend_python_class("pramod", "No")