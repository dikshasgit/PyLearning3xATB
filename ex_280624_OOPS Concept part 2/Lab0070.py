class VWOLoginPage:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def login_confirm(self):
        if self.__email == "mangesh@123" and self.__password == "123":
            print("You are allowed")
        else:
            print("Not allowed")


user1 = VWOLoginPage("deepak@345", "123")
user1.login_confirm()
user2 = VWOLoginPage("mangesh@123", "123")
user2.login_confirm()




