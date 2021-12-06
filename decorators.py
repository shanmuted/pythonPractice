'''print(dir())
num=20
def f1( ):
    n=10
    print("inside:",dir())
f1()
print("outside:",dir())'''
'''def fun(): #store fuction in variable
    print("hi")
g=fun
print(g)
g()'''
'''def outer():
    x=3
    def inner():
        y=3
        res=x+y
        return res
    return inner
a=outer()
print(a())
print(a.__name__)'''
#decorators
'''def dec(func):
    def inner():
        str1=func()
        return str1.upper().split()
    return inner()
@dec
def printstr():
    return "good evening"
print(printstr)'''
def num(func):
    def sqr():
        st=func()
        return st*4*st
    return sqr
@num
def prnt():
    return 10
print(prnt())