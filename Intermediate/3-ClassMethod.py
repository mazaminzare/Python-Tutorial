#decorator


class User:
    activeUsers = 0 # specific attribbute of class
    def __init__(self,name, family):
        self.name=name
        self.family=family
        User.activeUsers+=1
        print(f"{self.name} is logged in")
    def logOut(self):
        User.activeUsers-=1
        print(f"{self.name} logged out")

    @classmethod
    def getActiveUserCount(cls):
        print(f"there are currently {cls.activeUsers} active users")
    @classmethod
    def from_string(User,string_data):
        name, family=string_data.split(",")
        # return cls(data[0], data[1])
        return User(name,family)

# cls is equal to below => me =User() or introduce a instance manually
# but with classmethod is done automatically


User.getActiveUserCount()
me=User("Mohammad","zare")
you=User("sara","moradi")
print(User.activeUsers)
User.getActiveUserCount()

newInstance=User.from_string("mohammad,zare")
print(newInstance.name)
print(User.activeUsers)
