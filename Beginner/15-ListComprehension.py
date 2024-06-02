
myNumbers = [1,2,3,4,5,6]
print(myNumbers)
doubeld_numbers = [num * 2 for num in myNumbers]
print(doubeld_numbers)
myName="Mohammad"
namesCharacter= [char.upper() for char in myName]
print(namesCharacter)

print("=======================")
even =[num for num in myNumbers if num % 2 == 0]
odd = [num for num in myNumbers if num % 2 != 0]
print(f"the even number is{even}")
print(f"the odd number is{odd}")

newList = [num*2 if num%2==0 else num*3 for num in myNumbers]
print(newList)