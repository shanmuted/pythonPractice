a="ocean"
len=len(a)
for i in range(len):
    j=len-1-i
    for s in range(len):
        if(s==i or s==j):
            print(a[i],end="")
        else:
            print(" ",end="")
    print(" ")