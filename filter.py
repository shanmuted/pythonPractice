l=['thiru','andharu','tyson','timeandwater']
l=list(filter(lambda n : 'and' in n,l))
print(l)
#add17
l2=[1,2,3,7,8,6,5,37]
a=list(map(lambda n: n+17,l2))
print(a)
#prime
l2=[1,2,3,7,8,6,5,37]
def primecheck(n):
    if(n>1):
     for i in range(2,(n//2)+1):
        if (n%i==0):
            break
     else:
        return n
b=list(filter(primecheck,l2))
print(b)