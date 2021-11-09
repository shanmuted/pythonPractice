n=5
count=0
for i in range(1,100):
    for j in range(1,100):
       while(count<=n):  
         if(i%j==0):
            break
         else:
            print(i)
            count+=1
            
      
