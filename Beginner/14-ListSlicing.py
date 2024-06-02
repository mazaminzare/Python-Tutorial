
# list slicing => to make a copy of a list

myNumbers = [1,2,3,4,5,6,7,8,9]
# selectedNumber = myNumbers[1]
# print(selectedNumber)
# selectedNumber = myNumbers[1:7]
# some_list [start : end : step]
selectedNumbersFromList = myNumbers[1:7:2]
print(selectedNumbersFromList)
selectedNumbersFromList = myNumbers[1:]

print(selectedNumbersFromList)
selectedNumbersFromList = myNumbers[:]
print(selectedNumbersFromList)
print(myNumbers)
print(myNumbers == selectedNumbersFromList)
print(myNumbers is selectedNumbersFromList)


##################
colors = ["red", "green", "blue", "yellow", "orange"]
copyOfColors = colors[::-1]
colors.reverse()
print(colors)
print(copyOfColors)


myName = "MohammadAmin Zare"
print(myName[::-1])