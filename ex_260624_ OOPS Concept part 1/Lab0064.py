# Class - with i/p function

class student:

    def __init__(self):
        self.name = input("Enter your name - ")
        self.age = input("Enter your age - ")

    def display(self):
        print(f'Name is {self.name}, Age is {self.age}')


student1 = student()
student1.display()