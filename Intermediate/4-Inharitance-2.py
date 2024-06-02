# method resolution order

# __mro__
# mro()
# help(cls)

class A:
    def sayHello(self):
        print("hello python in A")
class B(A):
    pass
    # def sayHello(self):
    #     print("hello python in B")
class C(A):
    pass
    # def sayHello(self):
    #     print("hello python in C")
class D(B, C):
    pass
    # def sayHello(self):
    #     print("hello python in D")

item =D()
item.sayHello()