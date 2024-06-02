# iterable
# iterator
# iterate

numbers = [1, 2, 3, 4, 5, 6]
colors = ('red', 'green', 'blue')
numbs = {1, 2, 3, 4, 5, 6}

#
# for num in numbers:
#     print(num)

itreator = iter(numbers)
print(next(itreator))
print(next(itreator))
print(next(itreator))
print(next(itreator))
print(next(itreator))
print(next(itreator))
# print(next(itreator))

name = 'sara'
iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
# print(next(iterName))
print("===============")
iterName = iter(name)

while True:
    try:

        print(next(iterName))
    except:
        break


