# list
myNumbers = [1, 2, 3, 4, 5, 6]
names = ["Amin", "Hassan", "Mohsen"]
test = ["Python", True, 5,[4, 5, 6]]

soppingCart = [["item1", 3, 4500], ["item2", 5, 5000]]

myDictionary = {
    "name": "Item1",
    "count": 3,
    "price": 2500,
    3:"test"
}

myDictionary2= dict(name="new Dic",age=25)
print(myDictionary2)

print(myDictionary2["name"])
print(myDictionary["name"])

me = {
    "name":"Mohammad",
    "family":"Zare",
    "age":20
}

print("=============get value=============")
print(me.values())
print(me.keys())
for value in me.values():
    print(value)
print("============get key==============")
for key in me.keys():
    print(key)

print("============get value with key==============")

for key in me.keys():
    print(me[key])
print("===========with seperated item===============")
for key,value in me.items():
    print(f"the key is : {key}, and the Value is : {value}  ")
print("==========wiht items================")
for item in me.items():
    print(item)