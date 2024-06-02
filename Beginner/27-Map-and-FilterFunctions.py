# filter

numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda num:num%2==0, numbers)
odds = filter(lambda num:num%2!=0, numbers)
print(evens)
print(list(evens))
print(list(odds))

print("==============example=============")

users =[
    {"name":"mohammad",'shopCart':[]},
    {"name":"sara",'shopCart':['kotlin','vue']},
    {"name":"iman",'shopCart':[]},
]

result = filter(lambda user:len(user['shopCart'])==0,users)
print(list(result))
result2 = filter(lambda user:not user['shopCart'],users)
print(list(result2))

print("===== fusion of filter and map")

result3=map(lambda user:user['name'],
            filter(lambda user:not user['shopCart'],users)
            )
print(list(result3))

result4 = [user['name'] for user in users if len(user['shopCart'])==0]
print(result4)