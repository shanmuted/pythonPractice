class Student():
    def __init__(self,name,group):
        self.name = name
        self.group = group
class Marks(Student):
    def __init__(self,name,group,eng,maths,tamil):
        super().__init__(name,group)
        self.eng=eng
        self.maths=maths
        self.tamil=tamil
class Total(Marks):
    def __init__(self,name,group,eng,maths,tamil):
        super().__init__(name,group,eng,maths,tamil)
        total=self.eng+self.tamil+self.maths
        print("Name:",self.name)
        print("")

o1 = Total("jaya","BCA",32,43,54)
