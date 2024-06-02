# iterable can convert to iterator
# iterator can be iterated

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    print(num)

def square(num):
    return num ** 2

def my_for(iterable, func, func2):
    iterator = iter(iterable)
    while True:
        try:
            thing = (next(iterator))
        except:
            break
        else:
            out = func(thing)
            func2(out)


# my_for(numbers, print)
my_for(numbers, square, print)



