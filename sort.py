listt=[1,3,4,5,6,2]
newlist=[]
for i in range(len(listt)-1):
    for j in range (i+1,len(listt)):
        
        if  listt[i]<listt[j]:
            temp=listt[i]
            listt[i]=listt[j]
            listt[j]=temp
print(listt)            
        
