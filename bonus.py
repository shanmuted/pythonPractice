
bill=int(input("enter the bill amount"))
if(bill>=1000):
     bill= bill-(bill*0.1)
     print(bill)
elif(bill>=2000):
      bill=bill-(bill*0.2)
      print(bill)
elif(bill>=3000):
     bill=bill-(bill*0.25)
     print(bill)
else:
     print(bill)
