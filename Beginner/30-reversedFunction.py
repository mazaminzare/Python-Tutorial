numbers = [1,2,3,4,5,6,7]

# numbers.reverse()
print(numbers)
print(list(reversed(numbers)))
print(list(reversed("hello")))
print("hello"[::-1]) # slicing

nameRes=''
print(nameRes.join(list(reversed("hello"))))
