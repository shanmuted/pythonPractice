listt=[]
n=5
for a in range(n):
    b=input("enter")
    listt.append(b)
print(listt)
for i in range(len(listt)-1):
    for j in range (i+1,len(listt)):
        if  listt[i]<listt[j]:
            temp=listt[i]
            listt[i]=listt[j]
            listt[j]=temp
print(listt)