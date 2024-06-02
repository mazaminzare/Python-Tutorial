# map

numbers = [1, 2, 3, 4, 5]
doubles=[]
for num in numbers:
    doubles.append(num*2)

print(doubles)
print("========lambda===============")

doubles2=(map(lambda x:x *2,numbers))
print(type(doubles2))
print((doubles2))
print(list(doubles2))
print(list(doubles2))


print("===========other example")
names=["amin", "sara","sahar","milad"]
UpperNames= map(lambda name: name.upper(),names)
print(list(UpperNames))

print("with list comprehension")
uppersNames2=[(name.upper()) for name in names]
print(uppersNames2)

print("another example")

people = [
    {"name":"mohammad", 'family':"zare","age":23},
    {"name":"sara", 'family':"moradi","age":25},
    {"name":"iman", 'family':"madaeny","age":30},
]

families = map(lambda person:person['family'],people)
print(list(families))
