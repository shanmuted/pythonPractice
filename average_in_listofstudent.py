
n=int(input("enter"))
for i in range (n):
 a=input().split()
str=input()
if(str==a[0]):
 avg=(int(a[1])+int(a[2])+int(a[3]))/3
 f="{:.2f}".format(avg)
 print(f)



