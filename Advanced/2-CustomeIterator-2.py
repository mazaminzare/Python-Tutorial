class User:
    ActiveUsers = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        userDic = {'name': name, 'age': age}
        User.ActiveUsers.append(userDic)
        self.index = 0

    def log_out(self):
        print(f"{self.name} is logged out")
        currentUser = list(filter(lambda user: user['name'] == self.name, User.ActiveUsers))[0]
        User.ActiveUsers.remove(currentUser)
        print(currentUser)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index< len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration


person_1 = User('mohammad', 24)
person_2 = User('sara', 24)
person_3 = User('hosna', 54)

# person_2.log_out()
print(person_1.ActiveUsers)

for person in person_1:
    print(person)
