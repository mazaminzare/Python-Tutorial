
numbers = {1,2,3,'erd',4,5,'r'}
tuple=(1,2,3,4,5,6,4,3,3,)
setCreate=set(tuple)
print(numbers)
print(setCreate)
print(numbers)
print(2 in setCreate)
print("====================")
for item in numbers:
    print(item)

courses = ["kotlin", "vuejs","python",'ionic']
courses_set = set(courses)
print(courses_set)


numbers = {1,2,3,4,"2"}
numbers.add("amin")
print(numbers)
# if 2 in numbers:
#     numbers.remove(2)
#     print(numbers)

numbers.discard(4)
print(numbers)

copyNumbers = numbers.copy()
print(copyNumbers)

print(numbers.clear())

python={"ali", "milad", "mohammad", "sara"}
kotlin = {"mohammad", "ahmad", "reza", "ali"}

print(f"python union kotlin is {python | kotlin}")
print(f"python eshterak kotlin is {python & kotlin}")

print("==========================")

newSet = {x**2 for x in range(0,10)}
print(newSet)
characters = {char for char in "hello world"}
print(characters)