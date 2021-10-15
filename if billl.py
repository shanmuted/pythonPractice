bill=0
a=input("which size of pizza do u want? type 'small','medium' or 'large'\n")
if(a=='small'):
    bill+=30
    #print(bill)
elif(a=='medium'):
    bill+=40
    #print(bill)
elif(a=='large'):
    bill+=50
    #print(bill)
b=input("do you want pepperoni?\n")
if(a=='small' and b=='yes' ):
    bill+=10
    #print(bill)
elif(a=='medium' and b=='yes'):
    bill+=20
    #print(bill)
elif(a=='large' and b=='yes'):
    bill+=30
    #print(bill)
c=input("do you want cheese?\n")
if(c=='yes'):
 bill+=10
 print(bill)
else:
    print(bill)
