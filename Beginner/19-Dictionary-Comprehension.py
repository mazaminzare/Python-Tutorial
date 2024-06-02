# comprehension in list
# numbers = [1, 2, 3, 4, 5]
#
# doubled = [num*2 for num in numbers]
# print(doubled)

numbers = dict(first=1, second=2, third=3)
print(numbers)

squeredNumbers = {key: value ** 2 for key, value in numbers.items()}
print(squeredNumbers)
print(squeredNumbers is numbers)

simpleNumbers = {num: num for num in [1, 2, 3, 4]}
print(simpleNumbers)

simpleNumbers = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4]}
print(simpleNumbers)
