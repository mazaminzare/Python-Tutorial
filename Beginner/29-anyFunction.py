
numbers = [0, 0, 0, 1, 0]

print(any(numbers))
print(any([]))

numbers = [2,6,4,2,6,2,8]
print(any([num%2!=0 for num in numbers]))
