n=6
if(n>1):
 for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break
 else:
       print(n,"prime")
else:
    print("not prime")
