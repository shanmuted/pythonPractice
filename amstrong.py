num=int(input("enter the number:"))
digit=0
amg=0
copy=num
aa=str(num)
ln=len(aa)
#print(ln)
while(copy!=0):
  digit=copy%10
  #print(digit)
  amg+=digit**ln
  #print(amg)
  copy//=10
print(amg)

if(num==amg):
 print(num,"is amstrong")
else:
 print(num,"is not amstrong")   
