def squereofNumbers(inputData):
    output = [num ** 2 for num in inputData]
    return output


dataIn = range(6)
dataOut = squereofNumbers(dataIn)
print(dataOut)


def Sum(firstNumber, secondNumber):
    return firstNumber + secondNumber


print(f"sum is {Sum(5, 6)}")


def showFullName(firstname, lastname):
    return f"{firstname} {lastname}"


name = "Mohammad Amin"
family = "Zare"
print(showFullName(name, family))

person = {
    "name": "Mohammad",
    "family": "zare"
}
print(showFullName(person["name"], person["family"]))


def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
numbers = [1,2,3,4,5,6,7,8,9]
output= sum_odd_numbers(numbers)
print(output)

def is_even_number(number):
    if number % 2==0:
        return True
    return False


print(is_even_number(4))
print(is_even_number(5))