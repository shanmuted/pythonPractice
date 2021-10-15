a=input("enter the para:")

b=input("enter the word")
c=[]
for i in a.split():
    if i.startswith(b):
        c.append(i)

print(c)
      
