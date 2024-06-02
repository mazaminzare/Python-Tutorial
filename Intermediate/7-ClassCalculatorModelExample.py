class Calculator:
    def sum(self, a, b):
        print(f"{a} + {b} : {a + b}")

    def subtract(self, a, b):
        print(f"{a} - {b} : {a - b}")

    def multiply(self, a, b):
        print(f"{a} * {b} : {a * b}")

    def division(self, a, b):
        print(f"{a} / {b} : {a / b}")


myCalc = Calculator()
print(myCalc.sum(3, 4))
