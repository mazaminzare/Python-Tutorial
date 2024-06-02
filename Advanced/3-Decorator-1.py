def sum(number, func):
    total = 0
    for num in range(1, number + 1): # [1,2,3,4,5]
        total += func(num)

    return total


def square(x):
    return x ** 2

print(square(4))
print(sum(5,square))
# 1+2+3+4+5


