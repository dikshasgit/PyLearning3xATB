class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "pass123":
            print("You are allowed")
        else:
            print("Not allowed")


user1 = VWOLoginPage("mangesh@123", "pass123")
user1.login_confirm()

user2 = VWOLoginPage("pramod@123", 123)
user2.login_confirm()