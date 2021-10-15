n=[5,20,25,20,30,20]
for i in range (0,len(n-1)):
        x=n[i]
        if(x==20):
            n.pop(x)
print(n)
