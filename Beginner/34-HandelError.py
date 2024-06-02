try:
    print(myName)
except:
    print('an error occurd')


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return "no key found"
    except IndexError:
        return "index Error"
    finally:
        print("done function")


person = {"name": 'mohammad', 'family': 'zare'}
# print(person['age'])
print(get(person, 'age'))
maximumReach = 0
# while True:
#
#     if maximumReach < 3:
#         maximumReach += 1
#     else:
#         print('maximum number of enter inputs is reached')
#         break
#     try:
#         num = int(input("insert a number"))
#     except:
#         print("thats not a number")
#     else:
#         print("you have enter a number")
#         break
#     finally:
#         print("this is finally section")


def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError as err:
        print(err)
        return "Dont divide by zero Please"
    except TypeError as err:
        print(err)
        return "first and second number must be number"



print(divide(1, "22"))
