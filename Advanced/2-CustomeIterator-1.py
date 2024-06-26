class Counter:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += self.step
            return num
        raise StopIteration


# myCounter = Counter(1, 20, 2)
myCounter = Counter(1, 20)
iter(myCounter)
for num in myCounter:
    print(num)
