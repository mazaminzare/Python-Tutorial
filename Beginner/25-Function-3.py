
def exponent(num,power=2):
    return num**power

print(exponent(2,3))
print(exponent(2))

def showFullName(first="default",last="no Family"):
    return f"{first} {last}"

print(showFullName("amin"))
print(showFullName(last="Amin",first="mohammad"))