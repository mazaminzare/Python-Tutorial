
# range() => to create a list of numbers
# 1,2,3,...., 20

myNumbers = list(range(1, 10))
print(list(range(10)))
print(list(range(0, 100, 10)))
print(list(range(100, 1, -10)))
print(myNumbers)

for num in range(0,10):
    print("*" * num)

for num in range(10,0,-1):
    print("*" * num)

for num in range(10):
    string = ""
    for item in range(num):
        string = string + "*"
    print(string)
print('==================')
for num in range(1,11):
    if num % 2 == 1:
        for star in range(1,6):
            print("*" * star)
    if num % 2 == 0:
        for star in range(6, 1, -1):
            print("*" * star)
