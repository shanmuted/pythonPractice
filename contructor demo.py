class Demo:
    def __init__(self):
        print("constructor is working")
    def display(self):
        print("method is working")
    def __str__(self):#string
        return "helllo"
p1=Demo()
print(p1)