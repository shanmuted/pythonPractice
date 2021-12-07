class Teacher:
    def teach(self):
        print("os")
class Student1(Teacher):
    def mark1(self):
        print("12")
class Student2(Teacher):
    def mark2(self):
        print("45")
obj=Student1()
obj.mark1()
obj=Student2()
obj.mark2()
obj.teach()