a="ocean"
for i in range(len(a)):
    for j in range(len(a)):
        if(j==i):
            print(a[i],end="")
        elif(i+j== 4):
            print(a[j],end="")
        else:
            print(" ",end="")
    print(" ")