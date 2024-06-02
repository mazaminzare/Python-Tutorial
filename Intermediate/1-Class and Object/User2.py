
class User:
    def __init__(self,gotName, gotFamily, gotAge):
        self.name=gotName
        self.family=gotFamily
        self.age=gotAge

    def showFullName(self): #show_full_name
        return f"the name is {self.name} {self.family}"

    def useAgeStatus(self):
        return "adult" if self.age>18 else "not adult"

me=User("mohammad","zare",24)
you=User("Ali","Karimi",15)

print(me.showFullName())
print(you.showFullName())
print(me.useAgeStatus())