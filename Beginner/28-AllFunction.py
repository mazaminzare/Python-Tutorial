
numbers=[1,2,3,4,0]
print(all(numbers))
print(all([]))

print(all([num%2==0 for num in numbers]))
print(([num%2==0 for num in numbers]))
