a=[[1,["ocean","pondy"]],[2,["xx","yy"]]]
user=["name","place","age"]
b={}
for i in range(len(a)):
    for j in range(len(a[i])-1):
        b.update({a[i][j]:a[i][j+1]})
c=int(input("enter"))
ans=b[c]
for i in range(len(ans)):
    print(user[i],":",ans[i])