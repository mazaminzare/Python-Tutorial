class User():
    activeUsersCount = 0
    allowedUsers = ["mohammad", "milad", "sara", "iman"]
    loggedInUsers=[]
    def __init__(self, userName, userFamily):
        if userName not in User.allowedUsers:
            raise ValueError(f"the {userName} is not allowed")
        self.name = userName
        self.family = userFamily
        User.activeUsersCount += 1
        User.loggedInUsers.append(userName)
        print(f"user {self.name} is logged in")

    def logOut(self):
        print(f"{self.name} is logged out")
        User.activeUsersCount -= 1
        User.loggedInUsers.remove(self.name)


print(f"active users {User.activeUsersCount}")
mohammad = User("mohammad", "zare")
sara = User("sara", "karimi")

print(User.allowedUsers)
User.allowedUsers=["hossein","sara"]

print(mohammad.allowedUsers)
mohammad.allowedUsers=["mohammad","asghar"]
print(mohammad.allowedUsers)
print(User.allowedUsers)


# print(id(sara.activeUsersCount))
# print(id(mohammad.activeUsersCount))
# print(id(User.activeUsersCount))

# print(User.loggedInUsers)
#
# print(f"active users {User.activeUsersCount}")
# sara.logOut()
# mohammad.logOut()
# print(f"active users {User.activeUsersCount}")
# print(User.loggedInUsers)
# # user2 = User("ali", "karimi")

# print(mohammad.loggedInUsers==User.loggedInUsers)
# print(mohammad.loggedInUsers is User.loggedInUsers)