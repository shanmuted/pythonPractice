num=int(input("enter the num:"))
summ=0
for i in range(1,num+1):
    summ+=i
    if(i!=num):
        print(i,end="+")
    else:
        print(i,"=",summ)
    
