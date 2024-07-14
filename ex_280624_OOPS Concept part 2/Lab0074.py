class Password:

    def __init__(self, password):
        self.__password = password

    def get_password(self, if_auth):
        if if_auth:
            print(self.__password)
        else:
            print("Authentication failed")

    def set_password(self, password):
        if len(password) > 8:
            self.__password = password
            print(self.__password)
        else:
            print("Weak password try again")


user1 = Password("Hacker123")
user1.get_password(True)
user1.set_password("hsd")