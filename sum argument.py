class Overloading:
    def display(self,a=none,b=none,c=none):
        self.a=a
        self.b=b
        self.c=c
        if(a!=none and b!=none and c!=none):
           return a+b+c
        elif(a!=none and b!=none):
            return a+b
        else:
           return a
obj=Overloading()
obj.display(2,3,4)