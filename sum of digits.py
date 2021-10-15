num=int(input("enter the number"))
summ=0
for i in range(0,4):
   
   summ+=num%10
   num//=10

print(summ)          
   
