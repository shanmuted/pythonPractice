t=int(input("test case"))
h=1
for i  in range(t):
    n=int(input("no of cycle"))
    for h in range(n):
      if(n==0):
       h=h  
       #print(h)
      elif(n%2!=0):
       h*=2
       #print(h)
      else:
       h+=1

    print(h)      
 
