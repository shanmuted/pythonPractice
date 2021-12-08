class Odd:
    odd=1
    def oddnum(self):
        num=self.odd
        self.odd+=2
        print(num)
class Even:
    even=0
    def evennum(self):
        num=self.even
        self.even+=2
        print(num)
obj1=Odd()
obj2=Even()
a=int(input("enter"))
for i in range(a):
    testcase=input("enter").split()
    for j in range(int(testcase[1])):
        if testcase[0]=="odd":
            obj1.oddnum()
        else:
            obj2.evennum()