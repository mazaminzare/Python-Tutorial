
def buggy_function(a, b):
    result = a + b
    if result > 10:
        result = result / 2
    return result

print(buggy_function(5, 7))
