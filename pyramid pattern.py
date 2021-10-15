
n = int(input("Enter the number of rows:"))  
k = 2 * n -2 
for i in range(0, n):  
    for j in range(0, n+1):  
        print(" ",end="")  
    n = n - 2     
    for j in range(0, i + 1):  
        print("*", end="")  
    print("")  
