class A:
    def __init__(self):
        print("A is class")
class B(A):
    def __init__(self):
        super().__init__()#to call class A
        print("b is class")
p1=B()

