
listNumbers = [1,2,3,4,5,6]

tupleNumbers = (1,2,3,4,5,6,(1,21,5),3,4,5,6,7)
print(tupleNumbers[0])
print(3 in tupleNumbers)

newTuple = (1,2,3,4,5)
print(type(newTuple))

locations ={
    (35.6,45,74) : "Tehran",
    (35.54,34,24) : "Shiraz"
}

print(locations[((35.6,45,74))])

print("========================")

for num in tupleNumbers:
    print(num)
print("========================")
print(tupleNumbers.count(3))
print(tupleNumbers.index(3))

print(tupleNumbers[6])
print(tupleNumbers[6][1])