
me = {
    "name":"Mohammad",
    "family":"Zare",
    "age":23
}

isExist= "email" in me
print(isExist)

if "email" in me:
    print(me["email"])
else:
    print("there is no email key in me")

isNameExist = "Mohammad" in me.values()
print(isNameExist)
print(me)
# me.clear()
# print(me)
copy_me = me.copy()
print(copy_me)

print(me==copy_me)
print(me is copy_me)

newUser = {"name":"unknown", "family":"unknown"}

newUser_2 = {}.fromkeys("name","unknown")
print(newUser_2)
newUser_3 = {}.fromkeys(["name"],"unknown")
print(newUser_3)
newUser_4 = {}.fromkeys(["name", "family"], "unknown")
newUser_5 = dict.fromkeys(["name", "family"], "unknown")
print(newUser_4)
print(newUser_5)

print("==============================")
print(me["name"])
print(me.get("name"))

# print(me["email"])
print(me.get("email"))

isPhoneExist = me.get("phone")
print(isPhoneExist is None)