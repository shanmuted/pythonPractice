num=(input("enter the num:"))
i=0
summ=0
a=int(num)
while(a!=0):
    digit=a%10
    summ+=digit
    a//=10
    if(i<len(num)-1):
       print(num[i],end="+")
    else:
        print(num[i],"=",summ,end=" ")
    i=i+1    
    
