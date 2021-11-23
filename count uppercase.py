a=input("enter")
count=0
for i in a:
    if(i.isupper()):
        count+=1
print(count)
x=int(input())
y=int(input())

for i in range(x+1,y+1):
    if(i%2!=0):
        print(i,end=" ")
      
