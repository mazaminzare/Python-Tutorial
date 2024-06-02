
#List

item1 = "python"
item2 = "ionic"
item3 = "kotlin"
item4 = "JQuery"
myList = [item1, item2, item3, item4]
print(f"myList has {len(myList)}")

myRange = range(1,30)
print(f" My range is exist in {list(myRange)}")
print(f" your item found is: {myList[-1]}")  # could have error
print(f" your item found is: {myList[len(myList)-1]}")

isExistKotlin = "Kotlin" in myList
print(isExistKotlin)



isExistKotlin = "kwss" in myList
print(isExistKotlin)