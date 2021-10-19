series=input("enter the series").strip()
count=1
for i in range(len(series)-1):
    if(series[i]==series[i+1]):
     count+=1
    else:
        print(series[i],count,end="")
        count=1
print((series[i]+str(count)),end="")
        
