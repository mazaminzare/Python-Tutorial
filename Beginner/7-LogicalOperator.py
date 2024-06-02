
#logical Operator

# and, or, not

# and

userAge = 19
userGender = "male"

if userAge >=18 and userGender == "male":
    print("you have to go to soldiry")
else:
    print("you can stay home")

print(f" True and True:{True and True}")
print(f" True and False:{True and False}")
print(f" False and True:{False and True}")
print(f" False and False:{False and False}")


# or

weather="sunny"
if weather =="sunny" or weather == "cloudy":
    print("we can travel")
else:
    print("we can not travel")

print(f" True and True:{True or True}")
print(f" True and False:{True or False}")
print(f" False and True:{False or True}")
print(f" False and False:{False or False}")

# not
isBrotherComming = False

if not isBrotherComming :
    print("my sister said: i will come")


# 2< age< 8 => dollars
# age>= 65 => 5 dollars
# rest => 10 dollars

age = 65
if(age>=0 and age<=2) or (age>=8 and age<65 ):
    print("i should pay you 10 dollars")

if not((age>2 and age<8) or (age>=65)):
    print("i should pay you 10 dollars")
