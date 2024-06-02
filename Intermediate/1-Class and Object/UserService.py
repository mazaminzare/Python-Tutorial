class IUserService:
    def getAllUsers(self): raise NotImplementedError

    def getUserById(self): raise NotImplementedError

    def creatNewUser(self): raise NotImplementedError


class UserServiceBySql(IUserService):
    def getAllUsers(self):
        print("get all users from sql server")
    def getUserById(self):
        print("ge user by id from sql server")
    def  creatNewUser(self):
        print("create new users from sql server")

class UserServiceByOracle(IUserService):
    def getAllUsers(self):
        print("get all users from Oracle")
    def getUserById(self):
        print("ge user by id from Oracle")
    def  creatNewUser(self):
        print("create new users from Oracle")
userService=UserServiceBySql()
userService2=UserServiceByOracle()
userService.getAllUsers()
userService2.getAllUsers()