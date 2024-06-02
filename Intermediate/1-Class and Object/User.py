# _name => python private variable
# __name => name mangling
# ____name__

class User:
    def __init__(self, userName):
        self.userName = userName
        self._password = "123"
        self._email = "Amin@amin.com"
        self.__messeage = "i love python"
    #
    # def login(self, gotPassword):
    #     if self._password == gotPassword:
    #         print("login user")
    #     else:
    #         print("you are not logged in")


class Person:
    def __init__(self):
        self.__message = "test Message"


me = User("mohammad")
# print(me._email)
# print(me.login("123"))

print(me._User__messeage)
you=Person()
print(you._Person__message)
