n=5
for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print("1",end=" ")
        elif(i+j==n):
            print("2",end=" ")
        else:
            print("*",end=" ")