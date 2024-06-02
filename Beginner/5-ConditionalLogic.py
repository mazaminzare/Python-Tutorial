
print('enter your name :')
myName = input()
print(f"my name is {myName}")


print('==========================')
userRank = 4
if userRank == 2:
    print("you got silver medal")
if userRank == 1:
    print("you got gold medal")
    print("you are the best")
elif userRank==3:
    print("you got bronze medal")
else:
    print("you got no medal")

print('========================')

print('you got Gold Medal') if userRank == 1 else print("no medal")
