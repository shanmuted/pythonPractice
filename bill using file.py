n=int(input("enter"))
for i in range(n):
    a=input("enter").split()
    def even():
        b=int(a[i+1])
        for j in range(0,b*2,2):
            print(j)
    def  odd():
        c=int(a[i])
        for k in range(1,c*2,2):
            print(k)
    if(a[i]=="even"):
       even()
    else:
       odd()
