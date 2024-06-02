
me={
    "name": "mohammad",
    "family":"zare",
    "age": 25,
    "email": "mohammad@yahoo.com"
}
print(me)
# me.pop("age")
# result = me.pop("name")
# me.popitem()
print(me)
print("====================")
second = {"age":50}
second.update(me)
print(second)

print("==================")
second["name"] ="amin"
second["address"] ="khone"
print(second)