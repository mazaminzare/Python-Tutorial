from random import choice


def greet(person):
    def get_mood():
        msg = choice(("hello there ", 'go away ', 'goodbye '))
        return msg

    result = get_mood() + person
    return result


def greet2(person):
    def get_mood():
        msg = choice(("hello there ", 'go away ', 'goodbye '))
        res=msg+person
        return res

    return get_mood


print("return function from a function")
res = greet2("mohammad")
print(res())
print("=============function in function ===============")

print(greet("amin"))
