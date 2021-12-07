class Father:
    def work(self):
        print("father is working")

class Mother:
    def work(self):

        print("mother is cooking")
        super().work()
class Son(Mother,Father):
    def study(self):
        print("son is studying")
obj=Son()
obj.work()
