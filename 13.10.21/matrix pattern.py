
  
num=''
n=5
for i in range(5,0,-1):
    print('*'*(i-1),end='')
    num+=str(n+1-i)
    print(int(num))
