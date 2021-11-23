name=open("namelist.txt","r+")
a=input("enter the name:")
b=input("enter the password")
for i in name:
      if(i.split()[0]==a and i.split()[1]==b):
          print("not successful")
          break
else:
    name.write(a)
    name.write(" ")
    name.write(b)
    name.write("\n")
    print("successful")
