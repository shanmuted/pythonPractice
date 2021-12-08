class Overloading:
    def display(self,a=None,b=None,c=None):
        self.a=a
        self.b=b
        self.c=c
        if(a!=None and b!=None and c!=None):
           print(a+b+c)
        elif(a!=None and b!=None):
            print(a+b)
        else:
           print(a)
obj=Overloading()
obj.display(2,4)