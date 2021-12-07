class Mom:
    def cook(self):
        print("mother")
class Dad:
    def work(self):
        print("father")
class Son(Dad,Mom):
    def study(self):
        print("hari")
class Daughter(Dad,Mom):
     def style(self):
         print("girl")
obj=Daughter()
obj.cook()
obj.work()