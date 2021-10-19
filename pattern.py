n=5
for i in range(n):
    for j in range(n):
        if(i+j==n-1):
            print(1,end=" ")
        elif(i+j==n):
            print(2,end=" ")
        elif(i+j==n+1):
            print(3,end=" ")
        elif(i+j==n+2):
            print(4,end=" ")
        elif(i+j==n+3):
             print(5,end=" ")
        else:
            print("*",end=" ")
    print( )
