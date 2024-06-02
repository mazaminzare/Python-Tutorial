
numbers = [1,2,3,4,5,67,8,9]
chars = ['a','t','2']
myName='mostafa'
names=['mohammmad', 'ali', 'hassan','iman']
res=[len(name) for name in names]
print(res)
print(max(names,key=lambda n:len(n)))
print(min(names,key=lambda n:len(n)))
print(max(numbers))
print(min(numbers))